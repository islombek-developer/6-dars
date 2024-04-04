def f(date):
    year, month, day = map(int, date.split('-'))
    a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    b = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return b[month - 1] + day
    else:
        return a[month - 1] + day

sana = "2000-07-09"
print(f(sana))  
