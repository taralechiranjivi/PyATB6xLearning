import pytest
import allure
import requests

@allure.title("TC#1 - Verify the GET request.")
@allure.description("Verify that the GET request is basically successful and gives you 200 OK as a status.")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200


@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 404



#### More
import pytest
import allure
import requests
@allure.title("TC#1 - Verify that 2-2 == 0")
@allure.description("This is a BASIC Math Test")
@pytest.mark.tapas
def test_basic_math():
    assert 2-2 == 0


@allure.title("TC#2 - Verify that 3-3 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0













