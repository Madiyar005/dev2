import pytest
from app import AttendanceTracker

def test_add_record():
    tracker = AttendanceTracker()
    assert tracker.add_record("Асқар", True) == True
    assert tracker.records["Асқар"] == True

def test_get_attendance():
    tracker = AttendanceTracker()
    tracker.add_record("Мадина", False)
    assert tracker.get_attendance("Мадина") == False
    assert tracker.get_attendance("Белгісіз Студент") == None