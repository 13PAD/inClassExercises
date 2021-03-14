from datetime import datetime,date
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fullName = input("enter your full name")
name = fullName.split()
birthdate = input(" birthday,  using YY:MM:DD format")
birthday = birthdate.split(':')
birth = date(year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2]))
weekday = birth.weekday()
age = date.today() - birth
years = age.days / 365
year = round(years)

print("Welcome called {} you are turning /  have turned {} years old and you where born on a {}. Your family name is {}"
      .format(name[0].capitalize(), year, days[weekday], name[1].capitalize()))
