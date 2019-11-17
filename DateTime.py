from datetime import datetime
import random
from time import time as my_timer
import time
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=1, tm_wday=3, tm_yday=1, tm_isdst=0)
print(time.gmtime(1))
print()
# currenttime : time.struct_time(tm_year=2019, tm_mon=11, tm_mday=17, tm_hour=11, tm_min=51, tm_sec=33, tm_wday=6, tm_yday=321, tm_isdst=0)
print(time.localtime())
print()
print(time.time())  # no of time the epoc has started : 1573971777.0138555

time_here = time.localtime()
print(time_here)
print("year : ", time_here[0], time_here.tm_year)
print("month : ", time_here[1], time_here.tm_mon)
print("day : ", time_here[2], time_here.tm_mday)

#####################################################################################################################
# Time difference between two enters
print("*"*50)

input("press enter")
wait_tm = random.randint(1, 6)
time.sleep(wait_tm)
start_tm = my_timer()
input("Press enter again")
end_tm = my_timer()

# strftime converts a string to date
print("stsrted at : " + time.strftime("%X", time.localtime(start_tm)))
print("ended at : " + time.strftime("%X", time.localtime(end_tm)))

print("elapsed : {}".format(end_tm-start_tm))
#####################################################################################################################
s = datetime.today().second
print(s)
