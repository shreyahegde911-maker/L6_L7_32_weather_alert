
import pytest
from weather_alert import (
    wind_alert,
    rain_alert,
    heat_alert,
    overall_alert
)


# WIND ALERT - TRUE AND FALSE BRANCHES
def test_wind_all_branches():
    assert wind_alert(90) == "warning"
    assert wind_alert(70) == "watch"
    assert wind_alert(40) == "advisory"
    assert wind_alert(20) == "none"


# RAIN ALERT - ALL CONDITIONS
def test_rain_high_saturated():
    assert rain_alert(50, True) == "warning"

def test_rain_high_not_saturated():
    assert rain_alert(50, False) == "watch"

def test_rain_moderate_saturated():
    assert rain_alert(20, True) == "watch"

def test_rain_moderate_not_saturated():
    assert rain_alert(20, False) == "advisory"

def test_rain_low():
    assert rain_alert(5, False) == "none"


# HEAT ALERT - ALL CONDITIONS
def test_heat_humidity_above_40():
    assert heat_alert(40, 60) == "watch"

def test_heat_humidity_equal_40():
    assert heat_alert(40, 40) == "watch"

def test_heat_warning():
    assert heat_alert(45, 40) == "warning"

def test_heat_advisory():
    assert heat_alert(35, 40) == "advisory"

def test_heat_none():
    assert heat_alert(25, 40) == "none"


# OVERALL ALERT - ALL BRANCHES
def test_overall_empty():
    assert overall_alert([]) == "none"

def test_overall_higher_severity():
    assert overall_alert(["advisory", "warning"]) == "warning"

def test_overall_lower_severity():
    assert overall_alert(["warning", "none"]) == "warning"

def test_overall_equal_severity():
    assert overall_alert(["watch", "watch"]) == "watch"

def test_overall_invalid_alert():
    with pytest.raises(ValueError):
        overall_alert(["invalid"])
