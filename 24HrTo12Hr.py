# this python program simple converts the 24 hours to 12 hours format
import time
hours = int(time.strftime('%H'))
def timeFormat(a):
  while True:
    if a >= 24:
      print("olny time between 0 to 23 allowed")
      a= int(input("enter time again: "))
    elif a >=0 and a < 12:
     print("the time is :",a,"AM")
     break
    elif a == 12:
      print("the time is: ",a, "PM")
      break
    elif a > 12 and a <= 23:
      print("The Time is: ",a-12, "PM")
      break
    else:
      print("something went wrong")
      break

timeFormat(hours)