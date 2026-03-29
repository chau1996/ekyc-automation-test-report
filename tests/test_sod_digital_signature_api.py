import pytest

from data.headers import api_headers_sod
from data.url import SOD_DIGITAL_API_URL
from utils.json_helper import decode_base64_json
from utils.payload_loader import load_sod_payload
from utils.api_helper import send_post_request

@pytest.mark.tc1
def test_sodCoKySo_4_valid_input_should_return_success():
    payload = load_sod_payload()
    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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
def test_sodKiSo_5_invalid_partner_id_should_fail_verification():
    payload = load_sod_payload()
    headers = api_headers_sod.copy()
    headers["Transaction-Partner-ID"] = "invalid-partner-id"

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=headers)

    response_data = response.json()
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert response.status_code == 200
    assert response_data.get("message") == "IDG-00000000"
    assert obj.get("errorMessage") == "Xác thực chữ ký không thành công"
    assert obj.get("errorCode") == "VERIFY SIGNATURE FAIL"
    assert obj.get("status") == 400


@pytest.mark.tc3
def test_sodKiSo_6_invalid_partner_signature_should_fail_verification():
    payload = load_sod_payload()
    headers = api_headers_sod.copy()
    headers["Transaction-Partner-SIGNATURE"] = "invalid-partner-id"

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=headers)

    response_data = response.json()
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert response.status_code == 200
    assert response_data.get("message") == "IDG-00000000"
    assert obj.get("errorMessage") == "Xác thực chữ ký không thành công"
    assert obj.get("errorCode") == "VERIFY SIGNATURE FAIL"
    assert obj.get("status") == 400

@pytest.mark.tc4
def test_sodKiSo_7_partner_id_signature_not_matching_should_fail():
    payload = load_sod_payload()
    headers = api_headers_sod.copy()
    headers["Transaction-Partner-ID"] = "partner-A-id"
    headers["Transaction-Partner-Signature"] = "signature-of-partner-B"

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=headers)

    response_data = response.json()
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert response.status_code == 200
    assert response_data.get("message") == "IDG-00000000"
    assert obj.get("errorMessage") == "Xác thực chữ ký không thành công"
    assert obj.get("errorCode") == "VERIFY SIGNATURE FAIL"
    assert obj.get("status") == 400

@pytest.mark.tc5
def test_sodCoKySo_8_invalid_cccd_should_return_success():
    payload = load_sod_payload({
        "cccd" : "038195018166@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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
def test_sodCoKySo_9_invalid_sod_should_return_success():
    payload = load_sod_payload({
        "raw.sod" : "038195018166@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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

@pytest.mark.tc7
def test_sodCoKySo_10_invalid_device_type_should_return_success():
    payload = load_sod_payload({
        "deviceType" : "mobile@@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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
def test_sodCoKySo_11_invalid_device_name_should_return_success():
    payload = load_sod_payload({
        "deviceName" : "vnpay@@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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

@pytest.mark.tc9
def test_sodCoKySo_12_invalid_device_version_should_return_success():
    payload = load_sod_payload({
        "deviceVersion" : "deviceVersion@@@@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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

@pytest.mark.tc10
def test_sodCoKySo_13_invalid_reg_place_address_should_return_success():
    payload = load_sod_payload({
        "regPlaceAddress" : "regPlaceAddress@@@@@"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)

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

@pytest.mark.tc11
def test_sodKiSo_14_device_type_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "deviceType": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    #assert response.status_code == 400, f"Sai status code: {response.status_code}"
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceType" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"

@pytest.mark.tc12
def test_sodKiSo_15_device_name_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "deviceName": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    #assert response.status_code == 400, f"Sai status code: {response.status_code}"
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceName" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"


@pytest.mark.tc13
def test_sodKiSo_16_device_version_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "deviceVersion": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceVersion" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"

@pytest.mark.tc14
def test_sodKiSo_17_reg_place_address_version_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "regPlaceAddress": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "regPlaceAddress" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"

@pytest.mark.tc15
def test_sodKiSo_18_cccd_version_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "cccd": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "cccd" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"

@pytest.mark.tc16
def test_sodKiSo_19_sod_version_blank_should_return_validation_error():
    payload = load_sod_payload(overrides={
        "raw.sod": ""
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "raw.sod" and "không được bỏ trống" in f.get("message", "")
        for f in fields
    ), f"Sai thông báo lỗi trong messageFields: {fields}"

@pytest.mark.tc17
def test_sodKiSo_20_remove_device_type_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceType"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceType" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc18
def test_sodKiSo_21_remove_device_name_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceName"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceName" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc19
def test_sodKiSo_22_remove_device_version_should_return_error():
    payload = load_sod_payload(remove_fields=["deviceVersion"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "deviceVersion" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc20
def test_sodKiSo_23_remove_reg_place_address_should_return_error():
    payload = load_sod_payload(remove_fields=["regPlaceAddress"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "regPlaceAddress" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc21
def test_sodKiSo_24_remove_cccd_should_return_error():
    payload = load_sod_payload(remove_fields=["cccd"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "cccd" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc22
def test_sodKiSo_25_remove_cccd_should_return_error():
    payload = load_sod_payload(remove_fields=["raw.sod"])

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    assert response_data.get("message") == "IDG-00000400"
    assert response_data.get("errorCode") == "INVALIDDATA"
    assert response_data.get("errorMessage") == "Dữ liệu lỗi"
    assert response_data.get("statusCode") == "400 BAD_REQUEST", f"Sai statusCode: {response_data.get('statusCode')}"
    assert response_data.get("status") == 400, f"Sai status: {response_data.get('status')}"

    # Kiểm tra messageFields chứa lỗi về deviceType
    fields = response_data.get("messageFields", [])
    assert any(
        f.get("fieldName") == "raw.sod" and "không được null" in f.get("message", "")
        for f in fields
    ), f"Sai messageFields: {fields}"

@pytest.mark.tc23
def test_sodKiSo_26_remove_cccd_should_return_error():
    payload = load_sod_payload({
        "cccd": "001300031124"
    })

    response = send_post_request(SOD_DIGITAL_API_URL, payload=payload, headers=api_headers_sod)
    response_data = response.json()

    # Kiểm tra phản hồi lỗi dữ liệu
    decoded = decode_base64_json(response_data.get("dataBase64"))
    obj = decoded.get("object", decoded)

    assert response_data.get("message") == "IDG-00000000", f"Sai message: {obj.get('message')}"
    assert obj.get("errorMessage") == "Xác minh thành công", f"Sai errorMessage: {obj.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", f"Sai errorCode: {obj.get('errorCode')}"
    assert obj.get("status") == 200, f"Sai status: {obj.get('status')}"