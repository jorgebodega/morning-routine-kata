from src.morning_routine import MorningRoutine


def test_do_exercise():
    morning_routine = MorningRoutine()

    result = morning_routine.what_should_i_do_now()

    assert result == "Do exercise"
