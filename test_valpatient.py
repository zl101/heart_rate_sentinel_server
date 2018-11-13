from valpatient import validatePatient
import pytest


@pytest.mark.parametrize("testinput,expected", [
    ([], -1),
    ({"patient_id": "10", "attending_email": "blah", "user_age": "20"}, 1),
    ({"patient_id": "10",  "user_age": "20"}, -1),
    ({"attending_email": "blah", "user_age": "20"}, -1),
    ({"patient_id": "10", "attending_email": "blah"}, -1),
    ({"patient_id": "-10", "attending_email": "blah", "user_age": "20"}, -1),
    ({"patient_id": "10", "attending_email": "blah", "user_age": "-20"}, -1),
])
def test(testinput, expected):
    res = validatePatient(testinput)
    assert res == expected
