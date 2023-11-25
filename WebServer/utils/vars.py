from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    DATABASE_URL=environ.get("DATABASE_URL")
    SESSION_NAME=environ.get("SESSION_NAME")
    HAS_SSL = str(environ.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(environ.get("FQDN"))
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(environ.get("PORT2"))
        )
    PORT=environ.get("PORT", None)