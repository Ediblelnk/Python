"""
This program is designed as practice for working with files and formatting.
Functionality:
  Create a task with a name, due-date, listname, and special notes
  Delete a task
  Create a list
  Have various settings that can be changed in the program
"""
import os

class _spaces():
  name = 20
  month = 6
  day = 6
  year = 8
  group = 10
  notes = 30

class Task():
  groups = ['']
  months = 'jan.feb.mar.apr.may.jun.jul.aug.sep.oct.nov.dec'.split(sep='.')

  _days31 = 'jan.mar.may.jul.aug.oct.dec'.split(sep='.')
  _days30 = 'apr.jun.sep.nov'.split(sep='.')
  _days28 = 'feb'.split(sep='.')

  def __init__(self, name: str, due_date: list[str, int, int], group: str, notes: str):
    self.name: str = name
    self.due_date: list[str, int, int] = due_date
    self.group: str = group
    self.notes: str = notes

    self._validate_date(self.due_date)

  def __str__(self):
    return '- ' + self.name.ljust(_spaces.name) + self.date_str() + self.group.ljust(_spaces.group) + self.notes.ljust(_spaces.notes)

  def date_str(self):
    return self.due_date[0].ljust(_spaces.month) + str(self.due_date[1]).ljust(_spaces.day) + str(self.due_date[2]).ljust(_spaces.year)

  @classmethod
  def _validate_date(cls, date: list[str, int, int]):
    #ensure types
    date = [str(date[0])[:3], int(date[1]), int(date[2])]

    while not cls._is_year(date[2]):
      print(date)
      try:
        date[2] = int(input('INVALID DAY.\nPlease input a valid year: '))
      except ValueError as v:
        print(v)

    while not cls._is_month(date[0]):
      print(date)
      try:
        date[0] = input('INVALID MONTH.\nPlease input a valid month: ')[:3]
      except ValueError as v:
        print(v)
    
    while not cls._is_day(*date):
      print(date)
      try:
        date[1] = int(input('INVALID DAY.\nPlease input a valid day: '))
      except ValueError as v:
        print(v)
    
    return date

  @classmethod
  def _is_month(cls, month: str):
    if month[:3] in cls.months:
      return True
    return False

  @classmethod
  def _is_day(cls, month: str, day: int, year: int):
    if month in cls._days31 and 0 < day < 32:
      return True
    elif month in cls._days30 and 0 < day < 31:
      return True
    elif cls._is_leapyear(year) and month in cls._days28 and 0 < day < 30:
      return True
    elif not cls._is_leapyear(year) and month in cls._days28 and 0 < day < 29:
      return True
    return False

  @classmethod
  def _is_year(cls, year):
    if isinstance(year, int):
      return True
    return False

  @staticmethod
  def _is_leapyear(year: int):
    if year % 400 == 0:
      return True
    if year % 100 == 0:
      return False
    if year % 4 == 0:
      return True
    return False

def import_data(file):
  with open(file, 'r', encoding='UTF-8') as ofile:
    pass
    #lines = 

def main():
  t = Task('Do the Trash', ['oct', 19, 2022], 'Chores', 'make sure to replace the bags!')

  print(t)


if __name__ == '__main__':
  main()