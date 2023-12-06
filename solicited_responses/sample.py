from saml2.client import Saml2Client
from sp_config import SP_CONFIG
from saml2 import config as saml_config
from flask import Flask, redirect, request, session

config = saml_config.Config()
config.load(SP_CONFIG)
app = Flask(__name__)
sp = Saml2Client(config=config)

@app.route('/login')
def login():
    
    request_id, authn_request = sp.prepare_for_authenticate()
    
    print("Saving request id to session " + request_id)
 #   if not "saml2_outstanding_requests" in session:
 #       session['saml2_outstanding_requests'] = {}
    session['saml2_outstanding_requests'] = {request_id: "/success"}
    
    headers = dict(authn_request['headers'])
    return redirect(headers['Location'])

@app.route('/acs', methods=['POST'])
def acs():
    print("Parsing received response")
    authn_response = sp.parse_authn_request_response(request.form['SAMLResponse'], saml_config.BINDING_HTTP_POST, session['saml2_outstanding_requests'])
    print(authn_response)
    
    return redirect('/success' if authn_response else '/error')

@app.route('/success', methods=['GET']) 
def success():
    return "<h1>Authentication successful!</h1>"
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'memcached'

    app.run(debug=True)

