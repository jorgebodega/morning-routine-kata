from datetime import time


class MorningRoutine:
    def __init__(self, now: time) -> None:
        self.now = now

    def what_should_i_do_now(self) -> str:
        if time(6) <= self.now < time(7):
            return "Do exercise"
        if time(7) <= self.now < time(8):
            return "Read and study"

        return ""
