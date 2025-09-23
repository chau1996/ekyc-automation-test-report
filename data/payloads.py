import json
import os

def load_validdg_payload(overrides=None, remove_fields=None):
    with open(os.path.join(os.path.dirname(__file__), "validdg_payload.json"), encoding="utf-8") as f:
        payload = json.load(f)

    # Nếu có dữ liệu ghi đè thì áp dụng
    if overrides:
        for key, value in overrides.items():
            keys = key.split(".")
            ref = payload
            for k in keys[:-1]:
                ref = ref.setdefault(k, {})
            ref[keys[-1]] = value

    if remove_fields:
        for key in remove_fields:
            keys = key.split(".")
            ref = payload
            for k in keys[:-1]:
                ref = ref.get(k, {})
            ref.pop(keys[-1], None)

    return payload

def read_sod_from_file(filename):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()
