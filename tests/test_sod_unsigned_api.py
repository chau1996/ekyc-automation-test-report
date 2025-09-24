import pytest

from data.headers import api_headers_sod
from data.url import SOD_API_URL
from utils.json_helper import decode_base64_json
from utils.payload_loader import load_sod_payload
from utils.api_helper import send_post_request

@pytest.mark.tc1
def test_sodKhongKS_4_valid_input_should_return_success():
    payload = load_sod_payload()
    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc2
def test_sodKhongKS_5_invalid_cccd_should_return_success():
    payload = load_sod_payload({
        "cccd" : "038195018166@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc3
def test_sodKhongKS_6_invalid_sod_should_return_success():
    payload = load_sod_payload({
       "raw.sod" : "038195018166@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Dữ liệu không toàn vẹn", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "DATA NOT INTERGRITY", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc4
def test_sodKhongKS_7_invalid_device_type_should_return_success():
    payload = load_sod_payload({
       "deviceType" : "038195018166@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc5
def test_sodKhongKS_8_invalid_device_name_should_return_success():
    payload = load_sod_payload({
       "deviceName" : "vnpay@@@@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc6
def test_sodKhongKS_9_invalid_device_version_should_return_success():
    payload = load_sod_payload({
       "deviceVersion" : "vnpay@@@@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc7
def test_sodKhongKS_10_invalid_reg_place_address_version_should_return_success():
    payload = load_sod_payload({
       "regPlaceAddress" : "vnpay@@@@@"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Lấy message ở cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Decode và kiểm tra các giá trị trong object
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"

@pytest.mark.tc8
def test_sodKhongKS_11_deviceType_empty_should_return_error():
    payload = load_sod_payload({
       "deviceType" : ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceType",
        "message": "deviceType không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc9
def test_sodKhongKS_12_deviceName_empty_should_return_error():
    payload = load_sod_payload({
       "deviceName" : ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceName",
        "message": "deviceName không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc10
def test_sodKhongKS_13_deviceVersion_empty_should_return_error():
    payload = load_sod_payload({
       "deviceVersion" : ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceVersion",
        "message": "deviceVersion không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc11
def test_sodKhongKS_14_regPlaceAddress_empty_should_return_error():
    payload = load_sod_payload({
       "regPlaceAddress" : ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "regPlaceAddress",
        "message": "regPlaceAddress không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"


@pytest.mark.tc12
def test_sodKhongKS_15_cccd_empty_should_return_error():
    payload = load_sod_payload({
        "cccd": ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "cccd",
        "message": "cccd không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc13
def test_sodKhongKS_16_sod_empty_should_return_error():
    payload = load_sod_payload({
        "raw.sod": ""
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "raw.sod",
        "message": "sod không được bỏ trống"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc14
def test_sodKhongKS_17_deviceType_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceType"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceType",
        "message": "deviceType không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc15
def test_sodKhongKS_18_deviceName_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceName"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceName",
        "message": "deviceName không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc16
def test_sodKhongKS_19_deviceVersion_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceVersion"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "deviceVersion",
        "message": "deviceVersion không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc17
def test_sodKhongKS_20_regPlaceAddress_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["regPlaceAddress"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "regPlaceAddress",
        "message": "regPlaceAddress không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc18
def test_sodKhongKS_21_cccd_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["cccd"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "cccd",
        "message": "cccd không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc19
def test_sodKhongKS_22_sod_remove_should_return_error():
    payload = load_sod_payload(remove_fields=["raw.sod"])

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Lấy full response
    response_data = response.json()

    #Kiểm tra mã lỗi HTTP
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    #Kiểm tra nội dung lỗi
    assert response_data.get("errorMessage") == "Dữ liệu lỗi", f"Sai errorMessage: {response_data.get('errorMessage')}"
    assert response_data.get("errorCode") == "INVALIDDATA", f"Sai errorCode: {response_data.get('errorCode')}"
    assert response_data.get("message") == "IDG-00000400", f"Sai message: {response_data.get('message')}"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    #Kiểm tra messageFields (chi tiết trường lỗi)
    message_fields = response_data.get("messageFields", [])
    expected_error = {
        "fieldName": "raw.sod",
        "message": "sod không được null"
    }
    assert expected_error in message_fields, f"Không khớp messageFields: {message_fields}"

@pytest.mark.tc20
def test_sodKhongKS_23_id_mismatch_with_other_fields_should_pass():
    payload = load_sod_payload({
        "cccd": "001300031124"
    })

    response = send_post_request(SOD_API_URL, payload=payload, headers=api_headers_sod)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    response_data = response.json()
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert response_data.get("message") == "IDG-00000000", f"Sai message: {obj.get('message')}"
    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"
