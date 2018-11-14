from istachy import checkTachy
import pytest


@pytest.mark.parametrize("testinput,expected", [
    (["0.00", "200"], 1),
    (["1.5", "190"], 1),
    (["1.5", "80"], -1),
    (["kakaka", "90.5"], 0),
    (["16.5", "80.0101"], -1)
])
def test(testinput, expected):
    res = checkTachy(testinput[0], testinput[1])
    assert res == expected
