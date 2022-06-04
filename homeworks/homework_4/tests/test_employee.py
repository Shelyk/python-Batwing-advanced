import pytest
import requests
from employee import Employee

@pytest.fixture
def employee_obj():
    """
    Test Employee Fixture
    """
    emp = Employee(first="John", last="Smith", pay=45000)
    return emp

def test_employee_init(employee_obj):
    employee_obj.first == "John"
    employee_obj.last == "Smith"
    employee_obj.pay == 45000

def test_email(employee_obj):
    assert employee_obj.email == "John.Smith@email.com"

def test_fullname(employee_obj):
    assert employee_obj.fullname == "John Smith"

def test_apply_raise(employee_obj):
    employee_obj.apply_raise() == 47250

emp = Employee("John", "Smith", 45000)

def test_mock_api_call(mocker):
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "Success"

    schedule = emp.monthly_schedule("June")
    mock_requests.assert_called_with("http://company.com/Smith/June")
    assert schedule == "Success"