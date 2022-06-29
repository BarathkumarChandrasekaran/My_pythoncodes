years = range(2022,2025)
cmonth=[("Januray",31),("February",28),("March",31),("April",30),("May",31),("June",30),("July",31),("August",31),("September",30),("October",31),("November",30),("December",31)]
lmonth=[("Januray",31),("February",29),("March",31),("April",30),("May",31),("June",30),("July",31),("August",31),("September",30),("October",31),("November",30),("December",31)]
yearlist =[]
for y in years:
    year = {}
    if (y%4 !=0) and (y%400 == y%100):
        for months,days in cmonth:
            if months not in year:
                year[months] = []
                for day in range(1,days+1):
                    year[months].append(day)
        yearlist.append(year)
    else:
        year={}
        for lmonths, ldays in lmonth:
            if lmonths not in year:
                year[lmonths] = []
                for day in range(1, ldays + 1):
                    year[lmonths].append(day)
        yearlist.append(year)
print(yearlist,end='')