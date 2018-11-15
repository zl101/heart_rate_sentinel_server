from intervalavg import intervalAvgHelper
import pytest
import datetime
dict1 = {"1": {"attending_email": "a", "user_age": "10"},
         "2": {"attending_email": "b", "user_age": "11"}}
dict2 = {"1": [{"heart_rate": "160.1",
                "datetime": datetime.datetime(2018, 1, 9, 11, 0, 36, 372339)},
               {"heart_rate": "100.1",
                "datetime": datetime.datetime(2018, 4, 9, 11, 0, 36, 372339)},
               {"heart_rate": "50",
                "datetime": datetime.datetime(2018, 12, 9, 6, 0, 36, 372339)}],
         "2": []}


@pytest.mark.parametrize("testinput,expected", [
    ({"patient_id": "1",
      "heart_rate_average_since": "2018-12-12 10:10:36.372339"},
     -1),
    ({"patient_id": "2",
      "heart_rate_average_since": "2018-03-11 10:10:36.372339"},
     -1),
    ({"patient_id": "1",
      "heart_rate_average_since": "2017-03-11 10:10:36.372339"},
     103.4),
    ({"patient_id": "1",
      "heart_rate_average_since": "2018-03-11 10:10:03.372339"},
     75.05),
    ({"patient_id": "ogogab",
      "heart_rate_average_since": "2017-03-11 10:10:35.372339"},
     -1),
    ({"blah": "1",
      "heart_rate_average_since": "2017-03-11 10:10:35.372339"},
     -1),
    ({"patient_id": "1",
      "heart_rate_average_since": "HAHAHA-03-11 10:10:35.372339"},
     -1),
    ({"patient_id": "1",
      "OOGABOOGA": "2018-03-11 10:10:35.372339"},
     -1)
])
def test(testinput, expected):
    res = intervalAvgHelper(testinput, dict1, dict2)
    assert res == expected or res+0.001 > expected or res-0.001 < expected
