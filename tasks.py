from datetime import datetime
class Task:
    def __init__(self, name, description,priority):
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.priority = priority
    def input(self):
        self.name = input("Enter the name of the task: ")
        self.description = input("Enter the description of the task: ")
        self.priority = input("Enter the priority of the task: ")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = date
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self, priority):
        self._priority = priority
    def __str__(self):
        return self.name + " - " + self.description + " - " + self.priority + " - " + self.date.strftime("%m/%d/%Y")
    def __eq__(self, other):
        return self.name == other.name and self.description == other.description
