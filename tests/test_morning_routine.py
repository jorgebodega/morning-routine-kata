from datetime import time

from src.morning_routine import MorningRoutine


def test_do_nothing_before_start_routine():
    morning_routine = MorningRoutine(time(5, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "No activity"


def test_do_exercise_at_start_of_range():
    morning_routine = MorningRoutine(time(6))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"


def test_do_exercise_at_end_of_range():
    morning_routine = MorningRoutine(time(6, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"


def test_read_at_start_of_range():
    morning_routine = MorningRoutine(time(7))

    result = morning_routine.what_should_i_do_now()

    assert result == "Read"


def test_read_at_end_of_range():
    morning_routine = MorningRoutine(time(7, 29, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Read"


def test_study_at_start_of_range():
    morning_routine = MorningRoutine(time(7, 30))

    result = morning_routine.what_should_i_do_now()

    assert result == "Study"


def test_study_at_end_of_range():
    morning_routine = MorningRoutine(time(7, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Study"


def test_have_breakfast_at_start_of_range():
    morning_routine = MorningRoutine(time(8))

    result = morning_routine.what_should_i_do_now()

    assert result == "Have breakfast"


def test_have_breakfast_at_end_of_range():
    morning_routine = MorningRoutine(time(8, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Have breakfast"


def test_do_nothing_after_end_routine():
    morning_routine = MorningRoutine(time(9))

    result = morning_routine.what_should_i_do_now()

    assert result == "No activity"


def test_do_nothing_at_mid_day():
    morning_routine = MorningRoutine(time(12))

    result = morning_routine.what_should_i_do_now()

    assert result == "No activity"
