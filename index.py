#coding:utf-8
def leap_year(year):#判斷平瑞年
  if year%4==0 and year%100!=0 or year%400==0:
    return True
  else:
    return False
def getMonthDays(year,month):#得到每個年份每月的天數
  days = 31
  if month == 2 :
    if leap_year(year):
      days=29
    else:
      days=28
  elif month==4 or month==6 or month==9 or month==11:
    days=30
  return days
 
def getTotalDays(year,month):#計算星期
  totalDays=0
  for i in range(1,year):
    if leap_year(i):
      totalDays += 366
    else:
      totalDays += 365
  for i in range(1,month):
    totalDays +=getMonthDays(year,i)
  return totalDays
year=input("輸入年份：")
month = input("請輸入月：")
iCount = 0
print "日\t一\t二\t三\t四\t五\t六"
i=1
for i in range((getTotalDays(year,month)%7)+1):
    print '\t',
    iCount+=1
for i in range(1,getMonthDays(year,month)+1):
    print i,'\t',
    iCount +=1
    if iCount%7 == 0 :
      print ''