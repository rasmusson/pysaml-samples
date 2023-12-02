from saml2.client import Saml2Client
from sp_config import SP_CONFIG
from saml2 import config as saml_config
from flask import Flask, redirect, request

config = saml_config.Config()
config.load(SP_CONFIG)
app = Flask(__name__)
sp = Saml2Client(config=config)

@app.route('/login')
def login():
    request_id, authn_request = sp.prepare_for_authenticate()
    headers = dict(authn_request['headers'])
    return redirect(headers['Location'])

@app.route('/acs', methods=['POST'])
def acs():
    authn_response = sp.parse_authn_request_response(request.form['SAMLResponse'], saml_config.BINDING_HTTP_POST)
    print(authn_response)
    return redirect('/success' if authn_response else '/error')

@app.route('/success', methods=['GET']) 
def success():
    return "<h1>Authentication successful!</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)

