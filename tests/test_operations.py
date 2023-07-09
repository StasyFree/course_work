import pytest
from src.operations import Operation


@pytest.fixture
def element_creation():
    state = 'EXECUTED'
    date = '2019-08-26T10:50:58.294041'
    amount = '5000'
    currency = 'руб'
    description = 'перевод'
    recipient = 'VISA 1234'
    destination = 'VISA 5455'
    return state, date, amount, currency, description, recipient, destination


def test_init(element_creation):
    state, date, amount, currency, description, destination, recipient = element_creation
    operation = Operation(state, date, amount, currency, description, recipient, destination)
    assert operation.state == state
    assert operation.date == date
    assert operation.amount == amount
    assert operation.currency == currency
    assert operation.destination == destination
    assert operation.description == description
    assert operation.recipient == recipient


def test_change_date(element_creation):
    state, date, amount, currency, description, destination, recipient = element_creation
    operation = Operation(state, date, amount, currency, description, recipient, destination)
    operation.change_date()
    assert operation.date.year == 2019
    assert operation.date.day == 26
    assert operation.date.microsecond == 294041

