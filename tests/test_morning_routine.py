from datetime import time

from src.morning_routine import MorningRoutine


def test_do_exercise_at_start_of_range():
    morning_routine = MorningRoutine(time(6))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"


def test_do_exercise_at_end_of_range():
    morning_routine = MorningRoutine(time(6, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"


def test_read_and_study_at_start_of_range():
    morning_routine = MorningRoutine(time(7))

    result = morning_routine.what_should_i_do_now()

    assert result == "Read and study"


def test_read_and_study_at_end_of_range():
    morning_routine = MorningRoutine(time(7, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Read and study"


def test_have_breakfast_at_start_of_range():
    morning_routine = MorningRoutine(time(8))

    result = morning_routine.what_should_i_do_now()

    assert result == "Have breakfast"


def test_have_breakfast_at_end_of_range():
    morning_routine = MorningRoutine(time(8, 59, 59))

    result = morning_routine.what_should_i_do_now()

    assert result == "Have breakfast"
