import json
import pytest

from data.headers import api_headers_validdg
from data.payloads import load_validdg_payload, read_sod_from_file
from data.url import VALIDDG_API_URL
from utils.api_helper import send_post_request
from utils.json_helper import decode_base64_json

@pytest.mark.tc1
def test_validdg_api_success():
    payload = load_validdg_payload()
    response = send_post_request(VALIDDG_API_URL, payload = payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã phản hồi
    assert response.status_code == 200, "Status Code khác 200"

    # Giải mã dataBase64
    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)

    # Truy cập object bên trong payload giải mã
    obj = decoded.get("object", {})

    assert obj.get("errorMessage") == "Dữ liệu toàn vẹn", f"errorMessage sai: {decoded.get('errorMessage')}"
    assert obj.get("errorCode") == "SUCCESS", "errorCode sai"
    assert obj.get("status") == 200, "status sai"
    assert obj.get("msgid") is not None, "msgid không tồn tại"

@pytest.mark.tc2
def test_validdg_api_invalid_com():
    payload = load_validdg_payload({
        "raw.com": "invalid_com"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)

    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc3
def test_validdg_api_invalid_raw():
    payload = load_validdg_payload({
        "raw.sod": "invalid_com"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc4
def test_validdg_api_invalid_dg1():
    payload = load_validdg_payload({
        "raw.dg1": "INVALID_DG1_VALUE$#@"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc5
def test_validdg_api_invalid_dg2():
    payload = load_validdg_payload({
        "raw.dg2": "INVALID_DG2_VALUE$#@"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc6
def test_validdg_api_invalid_dg13():
    payload = load_validdg_payload({
        "raw.dg13": "INVALID_DG13_VALUE$#@"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc7
def test_validdg_api_invalid_dg14():
    payload = load_validdg_payload({
        "raw.dg14": "INVALID_DG14_VALUE$#@"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc8
def test_validdg_api_invalid_dg15():
    payload = load_validdg_payload({
        "raw.dg14": "INVALID_DG15_VALUE$#@"
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc9
def test_validdg_api_invalid_sod():
    sod_value = read_sod_from_file("sod/sod_invalid.txt")

    payload = load_validdg_payload({
        "raw.sod": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc10
def test_validdg_api_inconsistent_data():
    sod_value = read_sod_from_file("dg1/dg1_invalid.txt")
    payload = load_validdg_payload({
        "raw.dg1": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc11
def test_apiToanVen14_invalid_dg2_integrity():
    sod_value = read_sod_from_file("dg2/dg2_invalid.txt")
    payload = load_validdg_payload({
        "raw.dg2": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc12
def  test_apiToanVen15_invalid_dg13_integrity():
    sod_value = read_sod_from_file("dg13/dg13_invalid.txt")
    payload = load_validdg_payload({
        "raw.dg13": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc13
def  test_apiToanVen16_invalid_dg14_integrity():
    sod_value = read_sod_from_file("dg14/dg14_invalid.txt")
    payload = load_validdg_payload({
        "raw.dg14": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc14
def  test_apiToanVen17_invalid_dg15_integrity():
    sod_value = read_sod_from_file("dg15/dg15_invalid.txt")
    payload = load_validdg_payload({
        "raw.dg15": sod_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc15
def test_apiToanVen18_multiple_fields_from_A_should_fail_integrity():
    dg1_value = read_sod_from_file("dg1/dg1_invalid.txt")
    dg2_value = read_sod_from_file("dg2/dg2_invalid.txt")
    dg13_value = read_sod_from_file("dg13/dg13_invalid.txt")

    payload = load_validdg_payload({
        "raw.dg1": dg1_value,
        "raw.dg2": dg2_value,
        "raw.dg13": dg13_value
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200, "Status Code khác 200"

    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu không toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "DATA NOT INTERGRITY", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc16
def test_apiToanVen19_device_type_empty_should_fail():
    payload = load_validdg_payload({
        "deviceType": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc17
def test_apiToanVen20_device_name_empty_should_fail():
    payload = load_validdg_payload({
        "deviceName": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc18
def test_apiToanVen21_device_version_empty_should_fail():
    payload = load_validdg_payload({
        "deviceVersion": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc19
def test_apiToanVen22_com_empty_should_fail():
    payload = load_validdg_payload({
        "raw.com": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc20
def test_apiToanVen23_sod_empty_should_fail():
    payload = load_validdg_payload({
        "raw.sod": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc21
def test_apiToanVen24_dg1_empty_should_fail():
    payload = load_validdg_payload({
        "raw.dg1": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc22
def test_apiToanVen25_dg2_empty_should_fail():
    payload = load_validdg_payload({
        "raw.dg2": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc23
def test_apiToanVen26_dg13_empty_should_fail():
    payload = load_validdg_payload({
        "raw.dg13": ""
    })

    print("Payload:", json.dumps(payload, ensure_ascii=False, indent=2))

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    # Kiểm tra body phản hồi
    body = response.json()

    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc24
def test_apiToanVen27_dg14_empty_should_fail():
    payload = load_validdg_payload({
        "raw.dg14": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 200, "Status code phải là 200 OK"

    # Kiểm tra body phản hồi
    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "SUCCESS", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

@pytest.mark.tc25
def test_apiToanVen28_dg15_empty_should_fail():
    payload = load_validdg_payload({
        "raw.dg15": ""
    })

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 200, "Status code phải là 200 OK"

    # Kiểm tra body phản hồi
    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "SUCCESS", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"


@pytest.mark.tc26
def test_apiToanVen29_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["deviceType"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc27
def test_apiToanVen30_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["deviceName"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc28
def test_apiToanVen31_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["deviceVersion"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc29
def test_apiToanVen32_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["raw.com"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc30
def test_apiToanVen33_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["raw.sod"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc31
def test_apiToanVen34_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["raw.dg1"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc32
def test_apiToanVen35_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["raw.dg2"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"


@pytest.mark.tc33
def test_apiToanVen36_deviceType_missing_should_fail():
    payload = load_validdg_payload(remove_fields=["raw.dg13"])

    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi
    assert response.status_code == 400, "Status code phải là 400 BAD_REQUEST"

    body = response.json()
    assert body.get("errorMessage") == "Dữ liệu lỗi", "Sai errorMessage"
    assert body.get("errorCode") == "INVALIDDATA", "Sai errorCode"
    assert body.get("message") == "IDG-00000400", "Sai message"
    assert body.get("statusCode") == "400 BAD_REQUEST", "Sai statusCode"
    assert body.get("status") == 400, "Sai status"

@pytest.mark.tc34
def test_apiToanVen37_deviceType_missing_should_fail():

    payload = load_validdg_payload(remove_fields=["raw.dg14"])
    response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 200, "Status code phải là 200 OK"

    # Kiểm tra body phản hồi
    data = response.json().get("dataBase64")
    decoded = decode_base64_json(data)
    target = decoded.get("object", decoded)

    assert target.get("errorMessage") == "Dữ liệu toàn vẹn", "Sai errorMessage"
    assert target.get("errorCode") == "SUCCESS", "Sai errorCode"
    assert target.get("status") == 200, "Sai status"

# @pytest.mark.tc35
# def test_apiToanVen38_deviceType_missing_should_fail():
#     payload = load_validdg_payload(remove_fields=["raw.dg15"])
#
#     response = send_post_request(VALIDDG_API_URL, payload=payload, headers=api_headers_validdg)
#
#     print("Status Code:", response.status_code)
#     print("Response Body:", response.json())
#
#     # Kiểm tra status code
#     assert response.status_code == 200, "Status code phải là 200 OK"
#
#     # Kiểm tra body phản hồi
#     data = response.json().get("dataBase64")
#     decoded = decode_base64_json(data)
#     target = decoded.get("object", decoded)
#
#     assert target.get("errorMessage") == "Dữ liệu toàn vẹn", "Sai errorMessage"
#     assert target.get("errorCode") == "SUCCESS", "Sai errorCode"
#     assert target.get("status") == 200, "Sai status"