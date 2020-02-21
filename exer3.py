# Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# Output
# Current date and time :
# 2020-02-12 08:41:39
