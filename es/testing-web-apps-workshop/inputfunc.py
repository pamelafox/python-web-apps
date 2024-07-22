import pytest

def input_number(message):
    user_input = int(input(message))
    return user_input


@pytest.fixture(scope='module')
def mock_input(monkeypatch):
    def fake_input(msg):
        return '5'
    monkeypatch.setattr('builtins.input', fake_input)

def test_input_int(mock_input):
    assert input_number('Enter num') == 5
    # assert type is int
    assert type(input_number('Enter num')) == int
    assert isinstance(input_number('Enter num'), int)
    # > < == != >= <=

def test_input_int2(mock_input):
    assert input_number('Enter num') == 5
    # assert type is int
    assert type(input_number('Enter num')) == int
    assert isinstance(input_number('Enter num'), int)
    # > < == != >= <=

@pytest.fixture(scope='session')
def fake_database_data():
    database.insert(my_fake_data.json)