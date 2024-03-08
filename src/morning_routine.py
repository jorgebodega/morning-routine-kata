from datetime import datetime, time


class Activity:
    def __init__(self, interval: tuple[time, time], name: str) -> None:
        self.interval = interval
        self.name = name

    def should_i_do_this(self, now: time) -> bool:
        return self.interval[0] <= now < self.interval[1]


class MorningRoutine:
    activities: list[Activity]

    def __init__(self, now: time = datetime.now().time()) -> None:
        self.now = now

        self.activities = []

    @staticmethod
    def create_with_my_activities(now: time = datetime.now().time()) -> "MorningRoutine":
        return (
            MorningRoutine(now)
            .add_activity((time(6), time(6, 45)), "Do exercise")
            .add_activity((time(6, 45), time(7)), "Take a shower")
            .add_activity((time(7), time(7, 30)), "Read")
            .add_activity((time(7, 30), time(8)), "Study")
            .add_activity((time(8), time(9)), "Have breakfast")
        )

    def add_activity(self, interval: tuple[time, time], name: str) -> "MorningRoutine":
        self.activities.append(Activity(interval, name))

        return self

    def what_should_i_do_now(self) -> str:
        for activity in self.activities:
            if activity.should_i_do_this(self.now):
                return activity.name

        return "No activity"
