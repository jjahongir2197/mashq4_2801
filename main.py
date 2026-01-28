class Habit:
    def __init__(self, name):
        self.name = name
        self.days = 0

    def mark_done(self):
        self.days += 1

    def info(self):
        return f"{self.name} | Kunlar: {self.days}"


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, h):
        self.habits.append(h)

    def report(self):
        for h in self.habits:
            print(h.info())


tracker = HabitTracker()

while True:
    print("\n1.Odat 2.Bajarildi 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        tracker.add_habit(Habit(input("Odat nomi: ")))
    elif c == "2":
        tracker.habits[int(input("Index: "))].mark_done()
    elif c == "3":
        tracker.report()
    elif c == "0":
        break
