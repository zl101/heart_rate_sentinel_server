from valhr import validateHeartRate
import pytest
dict = {"1": {"attending_email": "a", "user_age": "10"},
        "2": {"attending_email": "b", "user_age": "11"}}


@pytest.mark.parametrize("testinput,expected", [
    ([], -1),
    ({"patient_id": "1", "heart_rate": "60"}, 1),
    ({"patient_id": "1", "heart_rate": "-1"}, -1),
    ({"patient_id": "1", "heart_rate": "45.5"}, 1),
    ({"patient_id": "2", "heart_rate": "asd"}, -1),
    ({"patient_id": "3", "heart_rate": "50"}, -1),
    ({"patient_id": "1"}, -1),
    ({"heart_rate": "10"}, -1),
])
def test(testinput, expected):
    res = validateHeartRate(testinput, dict)
    assert res == expected
