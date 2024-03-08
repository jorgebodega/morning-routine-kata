from src.morning_routine import MorningRoutine
from datetime import time


def test_do_exercise():
    morning_routine = MorningRoutine(time(6,45))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"

def test_do_exercise_6_o_clock():
    morning_routine = MorningRoutine(time(6))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"


def test_read_and_study():
    pass