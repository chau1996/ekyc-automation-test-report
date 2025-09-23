import os
from dotenv import load_dotenv

load_dotenv()

api_headers_validdg = {
    "Authorization": f"bearer {os.getenv('AUTHORIZATION_TOKEN')}",
    "Token-id": os.getenv("TOKEN_ID"),
    "Token-key": os.getenv("TOKEN_KEY"),
    "mac-address": os.getenv("MAC_ADDRESS"),
    "Content-Type": os.getenv("CONTENT_TYPE", "application/json"),
}


api_headers_sod = {
    "Authorization": f"bearer {os.getenv('SOD_AUTHORIZATION')}",
    "Token-id": os.getenv("SOD_TOKEN_ID"),
    "Token-key": os.getenv("SOD_TOKEN_KEY"),
    "Content-Type": os.getenv("SOD_CONTENT_TYPE", "application/json"),
}
