from datetime import datetime

def calcAge(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = datetime.strptime(input("Enter you dirthadate (yyyy-mm-dd): "), '%Y-%m-%d')
print(calcAge(birthdate))
