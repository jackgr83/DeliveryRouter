import datetime


# Time complexity: O(1)
# Space complexity: O(1)
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hour(self, hour):
        self.hour += hour

    def add_minute(self, minutes):
        self.minute += minutes
        if self.minute > 59.0:
            self.add_hour(1)
        self.minute = self.minute % 60

    def add_second(self, seconds):
        self.second += seconds
        self.second = self.second % 60
        self.add_minute(int(self.second/60))

    def get_hour(self):
        return self.hour

    def get_min(self):
        return self.minute

    def get_sec(self):
        return self.second

    def __str__(self):
        return '{}'.format(datetime.time(self.hour, self.minute, self.second))
