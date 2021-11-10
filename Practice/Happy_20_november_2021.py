import datetime as dt

date = input("What's the date today? Ex: 2021-11-20 ")
date_obj = dt.datetime.strptime(date,'%Y-%m-%d')
date_obj = date_obj.strftime('%Y-%m-%d')
print("Input date: " + date_obj)

date_today = dt.date.today().strftime('%Y-%m-%d')
print("Today: " + date_today)

if date_obj == date_today:
    print("Input date is today date.")
    if date_today == '2021-11-20':
        print("Happy 21/10!")
        
else:
    print("Sorry, input date is not today date.")

