'''
Write a  Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

import datetime
date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
print(date2-date1)
