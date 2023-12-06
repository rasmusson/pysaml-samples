from saml2.config import Config
from saml2 import config as saml_config
from saml2.saml import NAMEID_FORMAT_EMAILADDRESS

# Replace SP_AUDIENCE and SP_ACS_URL with your specific values
SP_AUDIENCE = "urn:example:sp"
SP_ACS_URL = "http://localhost:8000/acs"

# SP Configuration
SP_CONFIG = {
    "entityid": SP_AUDIENCE,
    "service": {
        "sp": {
            "want_response_signed": False,
            "want_assertions_signed": False,
            "name_id_format": NAMEID_FORMAT_EMAILADDRESS,
            "signing_algorithm": "xmldsig-sha256",  # Specify the signing algorithm
            "endpoints": {
                "assertion_consumer_service": [
                    (SP_ACS_URL, saml_config.BINDING_HTTP_POST),
                    (SP_ACS_URL, saml_config.BINDING_HTTP_REDIRECT)

                ],
            },
            "allow_unsolicited": True,
            "require_signed_assertion": False,
            "require_signed_response": False,
        },
    },
    "metadata": {
        "local": ["metadata.xml"],    
    }
}
