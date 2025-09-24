import os

import requests

UPLOAD_API_URL = "https://sandbox-idg.vnpt.vn/file-service/v1/addFile"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMAGE_PATH = os.path.join(BASE_DIR, "data", "images", "img_face.jpg")

def upload_face_image_and_get_hash(file_path: str):
    headers = {
        "Authorization": "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4YzAzMTg0Zi02ZjE3LTRmNjMtYjViNy05Mzg2YjdmYTcxMGEiLCJhdWQiOlsicmVzdHNlcnZpY2UiXSwidXNlcl9uYW1lIjoidGVzdEBpZGcudm5wdC52biIsInNjb3BlIjpbInJlYWQiXSwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3QiLCJuYW1lIjoidGVzdEBpZGcudm5wdC52biIsInV1aWRfYWNjb3VudCI6IjhjMDMxODRmLTZmMTctNGY2My1iNWI3LTkzODZiN2ZhNzEwYSIsImF1dGhvcml0aWVzIjpbIlVTRVIiXSwianRpIjoiOGRhYjliMjItNDcyMi00MjMzLTk5NTYtMTllZTdjNmFmODY5IiwiY2xpZW50X2lkIjoiYWRtaW5hcHAifQ.YltzvGmtfQSulcuDCTp7-ytMQ2wI-qAlxxk95ssAbVV_UW79UE_SOgZ7J1qNj6R9LBqypaPomG_ZE8sXy-gaw3BvTa5RktFSCh9i9BweC89L4qcpcy7gSPspCAgBPl5zxLg0tr-7LG72KXYDWVbMp8ydf3y7_U6YApZ5I7XDqqi2YtY_YifcuTgUJVnizXN2XBJzVCp8t8vT1NQ1GXxxOP0ie4Pvv767dS_WYsildWS1qQWjglLJyQqaAchY84y9BZVB1rFlKWo7sKh003iItbKrFz27VxIUTlqCWWIVsX0zCFEDELONTD6AgD8dmXl0dyvcmJCySxglcH0WwXfyNQ",
        "Token-id": "988f19bf-bb27-4b07-9a13-405d8279385e",
        "Token-key": "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJuDAIbsbK3N1uVcyIdquDUoTQAGG4wwocu3EFDVtSqBFYXGnw/30E7nzQwylu/VWhDLJFLUwv+ZLMSws6Tc2GsCAwEAAQ==",
        "mac-address": "HUY_TEST-001"
    }

    # Các parameters giống JMeter
    data = {
        "title": "ocr face",
        "description": "ocr face old type",
        "type": "minio"
    }

    # File upload
    files = {
        "file": open(file_path, "rb")
    }

    response = requests.post(UPLOAD_API_URL, headers=headers, data=data, files=files)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code == 200:
        data = response.json()
        return data.get("object", {}).get("hash")
    else:
        print("Upload thất bại:", response.status_code, response.text)
        return None
