class clockTime:
    def __init__(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def setHours(self):
        return self.hours

    def setMinutes(self):
        return self.mins

    def setSeconds(self):
        return self.secs

    def setTime(self):
        return self.hours.mins.secs

    def showTime(self):
        print("Display Time:", self.hours + ":" + self.mins + ":" + self.secs)

if __name__=="__main__":
    user_hours = input("Enter hours:")
    user_mins = input("Enter minutes:")
    user_secs = input("Enter seconds:")

    clock = clockTime(user_hours, user_mins, user_secs)
    clock.showTime()