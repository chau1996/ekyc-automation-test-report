import os
from dotenv import load_dotenv

load_dotenv()

api_headers_validdg = {
    "Authorization": f"bearer {os.getenv('VALIDDG_AUTHORIZATION_TOKEN')}",
    "Token-id": os.getenv("VALIDDG_TOKEN_ID"),
    "Token-key": os.getenv("VALIDDG_TOKEN_KEY"),
    "mac-address": os.getenv("VALIDDG_MAC_ADDRESS"),
    "Content-Type": os.getenv("VALIDDG_CONTENT_TYPE", "application/json"),
}


api_headers_sod = {
    "Authorization": f"bearer {os.getenv('SOD_AUTHORIZATION_TOKEN')}",
    "Token-id": os.getenv("SOD_TOKEN_ID"),
    "Token-key": os.getenv("SOD_TOKEN_KEY"),
    "Content-Type": os.getenv("SOD_CONTENT_TYPE", "application/json"),
}

api_headers_faceid = {
    "Authorization": f"bearer {os.getenv('FACEID_AUTHORIZATION_TOKEN')}",
    "Token-id": os.getenv("FACEID_TOKEN_ID"),
    "Token-key": os.getenv("FACEID_TOKEN_KEY"),
    "mac-address": os.getenv("FACEID_MAC_ADDRESS"),
    "Content-Type": os.getenv("FACEID_CONTENT_TYPE", "application/json"),
}
