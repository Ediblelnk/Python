import time

print(f"{time.time()} is the time in seconds after the beginning of 1970")

print(f"\n{time.gmtime()} is the time formatted in Greenwich Mean Time")

print(f"\n{time.localtime()} is the time formatted in using local time zone")

print(f"\n{time.asctime()} is the time formatted in asctime which uses local time")

print(f"\n{time.ctime()} is the time formatted in ctime which uses local time")

time.sleep(5)

print(f"\n{time.asctime()} is the time after 5 seconds, which was caused by time.sleep(5)")

print(f"\n{time.timezone} is the time in seconds different from UTC")

print(f"\n{time.tzname} is a tuple of local non-DST timezone and local DST timezone")