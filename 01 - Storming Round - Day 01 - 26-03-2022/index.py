from datetime import datetime

# Parse the time strings
base=datetime(2021,10,1)
timeSinceBase=datetime(2021,10,4)-base

print(type(timeSinceBase))
reduce=timeSinceBase//7//4
print(datetime("2021-10-04"),timeSinceBase,reduce)
