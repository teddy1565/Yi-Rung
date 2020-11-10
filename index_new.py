#coding:utf-8
#演算法參考網站:http://4rdp.blogspot.com/2016/01/11-perpetual-calendar.html
def judge(years,month):#判斷輸入日期為新曆還是舊曆
    y = int(years)
    m = int(month)
    if m>12 or m<1:
        print ("range_out")
        return 0
    elif y<1:
        print ("range_out")
        return 0
    if y<=1582 and m<10:
        return old_calendar(y,m)
    elif y<10000 and y!=1582 or m!=10:
        return new_calendar(y,m)
    elif y<10000 and y==1582 and m==10:
        return change_cal(y,m)
    else:
        print ("range_out")
        return 0
def old_calendar(years,month):#舊制算法
    if month==1 or month==2:
        years -= 1
        c = int(years/100)
        y = int(years%100)
        month_d=31
        if month == 2:
            if (years+1)%4==0 and (years+1)%100!=0:
                month_d=29
            elif (years+1)%400==0:
                month_d=29
            else:
                month_d=28
        print("sun\tmon\ttue\twed\tthu\tfri\tsat")
        for i in range(1,month_d+1):
            w = (-c+y+int(y/4)+int((26*(month+12+1))/10)+i+4)%7
            if i==1:
                for gg in range(w):
                    print('\t',end=" ")
            if w==6:
                print (i,'\n',)
            else:
                print (i,'\t',end=" ")
    else:
        c = int(years/100)
        y = int(years%100)
        month_d=30
        if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            month_d=31
        print("sun\tmon\ttue\twed\tthu\tfri\tsat")
        for i in range(1,month_d+1):
            w = (-c+y+int(y/4)+int((26*(month+1))/10)+i+4)%7
            if i==1:
                for gg in range(w):
                    print('\t',end=" ")
            if w==6:
                print(i,'\n',)
            else:
                print(i,'\t',end=" ")
    return 0
def new_calendar(years,month):#新制算法
    if month==1 or month==2:
        years-=1
    c = int(years/100)#取西元年份前兩位
    y = int(years%100)#取西元年份後兩位
    month_d=31
    if month == 1 or month == 2:
        if month == 2:
            if (years+1)%4==0 and (years+1)%100!=0:
                month_d = 29
            elif (years+1)%400==0:
                month_d = 29
            else:
                month_d = 28
        print("sun\tmon\ttue\twed\tthu\tfri\tsat")
        for i in range(1,month_d+1):
            w = (-2*c+int(c/4)+y+int(y/4)+int(26*(month+12+1)/10)+i-1)%7
            if i==1:
                for gg in range(w):
                    print('\t',end=" ")
            if w==6:
                print (i,'\n',)
            else:
                print (i,'\t',end=" ")
    else:
        if month == 4 or month ==6 or month ==9 or month ==11:
            month_d=30
        print("sun\tmon\ttue\twed\tthu\tfri\tsat")
        for i in range(1,month_d+1):
            w = (-2*c+int(c/4)+y+int(y/4)+int(26*(month+1)/10)+i-1)%7
            if i==1:
                for gg in range(w):
                    print('\t',end=" ")
            if w==6:
                print(i,'\n',)
            else:
                print(i,'\t',end=" ")
    return 0
def change_cal(years,month):#如果選到的月份剛好是新舊交替之時
    print("sun\tmon\ttue\twed\tthu\tfri\tsat")
    print("\t1\t2\t3\t4\t15\t16")
    print("17\t18\t19\t20\t21\t22\t23")
    print("24\t25\t26\t27\t28\t29\t30")
    print("31",)
    return 0
while 1==1:#讓程式能夠一直循環執行直到使用者輸入否
    year=input("years: ")#使用者輸入的年份
    month =input("month: ")#使用者輸入的月份
    judge(year,month)#傳送至judge函數判斷
    print("\n")
    reserch = input("Continue?[Y/N]: ")#當程式執行過一次迴圈後詢問使用者是否還要繼續
    if reserch == "Y" or reserch == "y":
      continue
    elif reserch =="N" or reserch == "n":
      break
