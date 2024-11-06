class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    #staticmethod
    def from_string(date_string):
        day, month, year = map(int, date_string.split("-"))
        return Date(day, month, year)

    def display(self):
        print(f"{self.day:02d}-{self.month:02d}-{self.year}")

# Using the static method to create a Date instance from a string
date1 = Date.from_string("15-08-2021")
date1.display()  # Output: 15-08-2021
