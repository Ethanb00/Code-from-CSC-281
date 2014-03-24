# Ethan Bennett
# Your task is to create functions to print calendars.
# You may want to have a look at the python calendar module :-)
# For instance, here is the Unix calendar
#      March 2013       
# Su Mo Tu We Th Fr Sa  
#                 1  2  
#  3  4  5  6  7  8  9  
# 10 11 12 13 14 15 16  
# 17 18 19 20 21 22 23  
# 24 25 26 27 28 29 30  
# 31                    

#                             2013
#       January               February               March          
# Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
#        1  2  3  4  5                  1  2                  1  2  
#  6  7  8  9 10 11 12   3  4  5  6  7  8  9   3  4  5  6  7  8  9  
# 13 14 15 16 17 18 19  10 11 12 13 14 15 16  10 11 12 13 14 15 16  
# 20 21 22 23 24 25 26  17 18 19 20 21 22 23  17 18 19 20 21 22 23  
# 27 28 29 30 31        24 25 26 27 28        24 25 26 27 28 29 30  
#                                             31                    

#        April                  May                   June          
# Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
#     1  2  3  4  5  6            1  2  3  4                     1  
#  7  8  9 10 11 12 13   5  6  7  8  9 10 11   2  3  4  5  6  7  8  
# 14 15 16 17 18 19 20  12 13 14 15 16 17 18   9 10 11 12 13 14 15  
# 21 22 23 24 25 26 27  19 20 21 22 23 24 25  16 17 18 19 20 21 22  
# 28 29 30              26 27 28 29 30 31     23 24 25 26 27 28 29  
#                                             30                    

#         July                 August              September        
# Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
#     1  2  3  4  5  6               1  2  3   1  2  3  4  5  6  7  
#  7  8  9 10 11 12 13   4  5  6  7  8  9 10   8  9 10 11 12 13 14  
# 14 15 16 17 18 19 20  11 12 13 14 15 16 17  15 16 17 18 19 20 21  
# 21 22 23 24 25 26 27  18 19 20 21 22 23 24  22 23 24 25 26 27 28  
# 28 29 30 31           25 26 27 28 29 30 31  29 30                 
                                                                  

#       October               November              December        
# Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
#        1  2  3  4  5                  1  2   1  2  3  4  5  6  7  
#  6  7  8  9 10 11 12   3  4  5  6  7  8  9   8  9 10 11 12 13 14  
# 13 14 15 16 17 18 19  10 11 12 13 14 15 16  15 16 17 18 19 20 21  
# 20 21 22 23 24 25 26  17 18 19 20 21 22 23  22 23 24 25 26 27 28  
# 27 28 29 30 31        24 25 26 27 28 29 30  29 30 31              

import calendar
c = calendar.TextCalendar(calendar.SUNDAY)

def calMonth(month):
    # prints the month
    print(c.formatmonth(2013, month))
  
    
def calYear(year):
    # prints the year 
    print(c.formatyear(year, 2, 1, 1, 2))
    

    # Note that I did not provide tests cases.  You might want to ...
