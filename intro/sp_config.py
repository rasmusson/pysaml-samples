from saml2.config import Config
from saml2 import config as saml_config
from saml2.saml import NAMEID_FORMAT_UNSPECIFIED

# SP Configuration
SP_CONFIG = {
    "entityid": "urn:example:sp",
    "service": {
        "sp": {
            "want_response_signed": False,
            "want_assertions_signed": False,
            "name_id_format": NAMEID_FORMAT_UNSPECIFIED,
            "endpoints": {
                "assertion_consumer_service": [
                    ("http://localhost:8000/acs", saml_config.BINDING_HTTP_POST)
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