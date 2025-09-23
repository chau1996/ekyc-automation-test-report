import base64
import json

def decode_base64_json(base64_str):
    decoded_bytes = base64.b64decode(base64_str)
    decoded_str = decoded_bytes.decode('utf-8')
    return json.loads(decoded_str)
