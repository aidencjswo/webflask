import datetime
import time


date = time.localtime()
str = str(date.tm_year)+"/"+str(date.tm_mon)+"/"+str(date.tm_mday)
print(str)