import datetime
x=int(input("enter year: "))
y=int(input("enter month: "))
z=int(input("enter day: "))
print(datetime.date(x,y,z).isocalendar()[1])