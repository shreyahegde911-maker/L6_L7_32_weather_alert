
import pytest
from weather_alert import (
    wind_alert,
    rain_alert,
    heat_alert,
    overall_alert
)


# WIND ALERT TESTS
def test_wind_warning():
    assert wind_alert(89) == "warning"

def test_wind_watch():
    assert wind_alert(62) == "watch"

def test_wind_advisory():
    assert wind_alert(39) == "advisory"

def test_wind_none():
    assert wind_alert(10) == "none"


# RAIN ALERT TESTS
def test_rain_warning():
    assert rain_alert(50, True) == "warning"

def test_rain_watch_high_rain():
    assert rain_alert(50, False) == "watch"

def test_rain_watch_saturated():
    assert rain_alert(10, True) == "watch"

def test_rain_advisory():
    assert rain_alert(10, False) == "advisory"

def test_rain_none():
    assert rain_alert(5, False) == "none"


# HEAT ALERT TESTS
def test_heat_warning():
    assert heat_alert(45, 40) == "warning"

def test_heat_watch():
    assert heat_alert(40, 40) == "watch"

def test_heat_advisory():
    assert heat_alert(35, 40) == "advisory"

def test_heat_none():
    assert heat_alert(25, 40) == "none"

def test_heat_humidity_adjustment():
    assert heat_alert(40, 60) == "watch"


# OVERALL ALERT TESTS
def test_overall_warning():
    assert overall_alert(["advisory", "warning"]) == "warning"

def test_overall_none():
    assert overall_alert([]) == "none"

def test_overall_lower_severity():
    assert overall_alert(["none", "advisory"]) == "advisory"

def test_overall_invalid_alert():
    with pytest.raises(ValueError):
        overall_alert(["invalid"])
