import os

import pytest

from data.headers import api_headers_faceid
from data.url import FACEID_ADD_UPDATE_API_URL
from utils.api_helper import send_post_request
from utils.faceid_loader import load_faceid_payload
from utils.faceidfileservice import upload_face_image_and_get_hash, IMAGE_PATH



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FLOWER_IMAGE_PATH = os.path.join(BASE_DIR, "data", "images", "flower.png")


@pytest.mark.tc1
def test_addupdate4_full_info_should_return_success():
    hash_face = upload_face_image_and_get_hash(IMAGE_PATH)

    payload = load_faceid_payload(overrides={"img_face": hash_face})

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code
    assert response.status_code == 200, f"Sai status code: {response.status_code}"

    # Kiểm tra message cấp root
    assert response_data.get("message") == "IDG-00000000", f"Sai message: {response_data.get('message')}"

    # Kiểm tra object chính
    obj = response_data.get("object", {})
    assert obj.get("full_name") == "Yến", f"Sai full_name: {obj.get('full_name')}"
    assert obj.get("uuid_unit") == "0dc745cd-28ad-468c-9af4-2068000c0579", "Sai uuid_unit"

    # Kiểm tra thông tin trong customer_card
    card_info = obj.get("customer_card", {})
    assert card_info.get("card_id") == "031301000806", f"Sai card_id: {card_info.get('card_id')}"
    assert card_info.get("card_category_id") == 5, f"Sai card_category_id: {card_info.get('card_category_id')}"

    # Kiểm tra challengeCode có tồn tại
    assert "challengeCode" in response_data, "Thiếu challengeCode"

@pytest.mark.tc2
def test_addupdate5_uuid_unit_blank_should_return_error():
    hash_face = upload_face_image_and_get_hash(IMAGE_PATH)

    # Tạo payload với uuid_unit = ""
    payload = load_faceid_payload(overrides={
        "uuid_unit": "",
        "img_face": hash_face
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "uuidUnit", f"Sai fieldName: {field}"
    assert field.get("message") == "must not be blank", f"Sai message: {field}"


@pytest.mark.tc3
def test_addupdate6_img_face_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "img_face": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "imgFace", f"Sai fieldName: {field}"
    assert field.get("message") == "must not be blank", f"Sai message: {field}"

@pytest.mark.tc4
def test_addupdate7_verify_status_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "verify_status": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "verifyStatus", f"Sai fieldName: {field}"
    assert field.get("message") == "must not be null", f"Sai message: {field}"

@pytest.mark.tc5
def test_addupdate8_verify_status_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.card_id": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit

    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("message") == "Thông tin ID giấy tờ không được bỏ trống.", f"Sai message: {field}"

@pytest.mark.tc6
def test_addupdate9_card_category_id_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.card_category_id": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit

    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("message") == "Thông tin loại giấy tờ không được bỏ trống.", f"Sai message: {field}"

@pytest.mark.tc7
def test_addupdate10_full_name_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.full_name": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("message") == "Thông tin họ tên không được bỏ trống.", f"Sai message: {field}"

@pytest.mark.tc8
def test_addupdate11_dob_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.dob": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("message") == "Thông tin ngày sinh không được bỏ trống.", f"Sai message: {field}"

@pytest.mark.tc9
def test_addupdate12_result_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.result": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.result", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc10
def test_addupdate13_responseId_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.responseId": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.responseId", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc11
def test_addupdate14_exitcode_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.exitcode": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.exitcode", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc12
def test_addupdate15_time_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.time": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.time", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc13
def test_addupdate16_message_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.message": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.message", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc14
def test_addupdate17_signature_unit_blank_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.signature": ""
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "addCustomerCardDtoIn.resultC06.signature", f"Sai fieldName: {field}"
    assert field.get("message") == "Không được bỏ trống", f"Sai message: {field}"

@pytest.mark.tc15
def test_addupdate18_invalid_uuid_unit_should_return_not_found():
    payload = load_faceid_payload(overrides={
        "uuid_unit": "invalid-unit-id-123456"
    })
    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra status code lỗi
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra messageFields chứa thông tin lỗi uuidUnit
    assert response_data.get("error") == "Unit_not_found", f"Sai lỗi: {response_data.get('error')}"

@pytest.mark.tc16
def test_addupdate19_invalid_img_face_should_return_error():
    payload = load_faceid_payload(overrides={
        "img_face": "invalid_hash_or_url"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra lỗi "Image download failed"
    errors = response_data.get("errors", [])
    assert "Image download failed" in errors, f"Sai nội dung lỗi: {errors}"

@pytest.mark.tc17
def test_addupdate20_invalid_verify_status_should_return_error():
    payload = load_faceid_payload(overrides={
        "verify_status": 2
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    response_data = response.json()

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

    # Kiểm tra lỗi "Image download failed"
    fields = response_data.get("messageFields", [])
    field = fields[0] if fields else {}
    assert field.get("fieldName") == "verifyStatus", f"Sai fieldName: {field}"
    assert field.get("message") == "Nhận giá trị 0 hoặc 1", f"Sai message: {field}"

@pytest.mark.tc18
def test_addupdate21_invalid_card_id_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.card_id": "abc123"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc19
def test_addupdate22_invalid_card_category_id_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.card_category_id": 11
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc20
def test_addupdate23_invalid_result_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.result": "false"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc21
def test_addupdate24_invalid_responseId_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.responseId": "abcxnxnsmskskks"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc22
def test_addupdate25_invalid_exitcode_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.exitcode": 1
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc23
def test_addupdate26_invalid_time_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.time": 1
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc24
def test_addupdate27_invalid_message_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.message": "abc123656464"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc25
def test_addupdate28_invalid_signature_should_return_error():
    payload = load_faceid_payload(overrides={
        "customer_card.result_c06.signature": "abc123656464"
    })

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra mã lỗi trả về
    assert response.status_code == 400, f"Sai status code: {response.status_code}"

@pytest.mark.tc26
def test_addupdate29_img_is_not_face_should_return_400():
    hash_face = upload_face_image_and_get_hash(FLOWER_IMAGE_PATH)

    payload = load_faceid_payload(overrides={"img_face": hash_face})

    response = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload, headers=api_headers_faceid)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Kiểm tra status code
    assert response.status_code == 400, f"Sai status code: {response.status_code}"


@pytest.mark.tc27
def test_addupdate30_face_hash_duplicate_should_fail():
    hash_face = upload_face_image_and_get_hash(IMAGE_PATH)

    payload1 = load_faceid_payload(overrides={"img_face": hash_face})
    response1 = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload1, headers=api_headers_faceid)

    assert response1.status_code == 200, f"Lần đầu gọi thất bại: {response1.status_code}"

    payload2 = load_faceid_payload(overrides={"img_face": hash_face})
    response2 = send_post_request(FACEID_ADD_UPDATE_API_URL, payload=payload2, headers=api_headers_faceid)

    print("Status Code:", response2.status_code)
    print("Response Body:", response2.json())

    assert response2.status_code == 400, f"Sai status code: {response2.status_code}"

    # 4. Kiểm tra thông báo lỗi có chứa "Ảnh khuôn mặt đã tồn tại"
    error_message = response2.json().get("message", "")
    assert "Ảnh khuôn mặt đã tồn tại" in error_message or "idg-00020001" in error_message.lower(), f"Sai thông báo lỗi: {error_message}"