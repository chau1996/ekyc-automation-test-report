# import pytest
#
# from data.headers import api_headers_sod
# from data.url import SOD_DIGITAL_API_URL
# from utils.json_helper import decode_base64_json
# from utils.payload_loader import load_sod_payload
# from utils.api_helper import send_post_request
#
# @pytest.mark.tc1
# def test_sodCoKySo_4_valid_input_should_return_success():
#     payload = load_sod_payload()
#     response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
#
#     print("Status Code:", response.status_code)
#     print("Response Body:", response.json())
#
#     # Lấy full response
#     response_data = response.json()
#
#     # Kiểm tra status code
#     assert response.status_code == 200, f"Sai status code: {response.status_code}"
#
#     # Lấy message ở cấp root
#     assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"
#
#     # Decode và kiểm tra các giá trị trong object
#     decoded = decode_base64_json(response_data.get("dataBase64"))
#     obj = decoded.get("object", decoded)
#
#     assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
#     assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
#     assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"
#
#
# @pytest.mark.tc2
# def test_sodCoKySo_8_invalid_cccd_should_return_success():
#     payload = load_sod_payload({
#         "cccd" : "038195018166@@"
#     })
#
#     response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
#
#     print("Status Code:", response.status_code)
#     print("Response Body:", response.json())
#
#     # Lấy full response
#     response_data = response.json()
#
#     # Kiểm tra status code
#     assert response.status_code == 200, f"Sai status code: {response.status_code}"
#
#     # Lấy message ở cấp root
#     assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"
#
#     # Decode và kiểm tra các giá trị trong object
#     decoded = decode_base64_json(response_data.get("dataBase64"))
#     obj = decoded.get("object", decoded)
#
#     assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
#     assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
#     assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"
#
# @pytest.mark.tc3
# def test_sodCoKySo_9_invalid_sod_should_return_success():
#     payload = load_sod_payload({
#         "raw.sod" : "038195018166@@"
#     })
#
#     response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
#
#     print("Status Code:", response.status_code)
#     print("Response Body:", response.json())
#
#     # Lấy full response
#     response_data = response.json()
#
#     # Kiểm tra status code
#     assert response.status_code == 200, f"Sai status code: {response.status_code}"
#
#     # Lấy message ở cấp root
#     assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"
#
#     # Decode và kiểm tra các giá trị trong object
#     decoded = decode_base64_json(response_data.get("dataBase64"))
#     obj = decoded.get("object", decoded)
#
#     assert obj.get("errorMessage") == "Dữ liệu không toàn vẹn", f"Sai errorMessage: {obj.get('errorMessage')}"
#     assert obj.get("errorCode") == "DATA NOT INTERGRITY", f"Sai errorCode: {obj.get('errorCode')}"
#     assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"