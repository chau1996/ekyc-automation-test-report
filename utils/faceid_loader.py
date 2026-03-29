import json
import os

def load_faceid_payload(overrides=None, remove_fields=None):
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "add_update_faceid_payload.json")
    )

    with open(file_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    # Ghi đè các giá trị nếu có overrides
    if overrides:
        for key, value in overrides.items():
            keys = key.split(".")
            ref = payload
            for k in keys[:-1]:
                ref = ref.setdefault(k, {})
            ref[keys[-1]] = value

    # Xóa các trường nếu có remove_fields
    if remove_fields:
        for key in remove_fields:
            keys = key.split(".")
            ref = payload
            for k in keys[:-1]:
                ref = ref.get(k, {})
            ref.pop(keys[-1], None)

    return payload