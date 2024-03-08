from datetime import datetime, time


class MorningRoutine:
    def __init__(self, now: time = datetime.now().time()) -> None:
        self.now = now

    def what_should_i_do_now(self) -> str:
        activities = {
            (time(6), time(7)): "Do exercise",
            (time(7), time(7, 30)): "Read",
            (time(7, 30), time(8)): "Study",
            (time(8), time(9)): "Have breakfast",
        }

        for hour_range, activity in activities.items():
            start, end = hour_range
            if start <= self.now < end:
                return activity

        return "No activity"
