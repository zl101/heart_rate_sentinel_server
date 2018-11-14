from valpid import validatePid
import pytest
dict1 = {"1": {"attending_email": "a", "user_age": "10"},
         "2": {"attending_email": "b", "user_age": "11"}}
dict2 = {"1": [{"heart_rate": "160.1"}, {"heart_rate": "50"}],
         "2": []}


@pytest.mark.parametrize("testinput,expected", [
    ([], -1),
    ("1", 1),
    ("2", -1),
    ("3", -1),
    ("ooggabbooga", -1)
])
def test(testinput, expected):
    res = validatePid(testinput, dict1, dict2)
    assert res == expected
