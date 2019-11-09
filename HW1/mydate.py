# mydate.py
# Bowen Zhang
# bz896
# Homework 01

import random

months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_valid_month_num(n):
    if n >= 1 and n <= 12:
        return True
    else:
        return False

def month_num_to_string(month_num):
    if type(month_num) != int:
        return None
    elif is_valid_month_num(month_num):
        return months[month_num - 1]
    else:
        return None
    
def date_to_string(date_list):
    return month_num_to_string(date_list[0]) +' '+ str(date_list[1]) 
    
def dates_to_strings(list_of_date_lists):
    result = []
    for x in list_of_date_lists:
        result.append(date_to_string(x))
    return result
    
def remove_years(list_of_date_lists):
    result = []
    for x in list_of_date_lists :
        result.append([x[1], x[2]])
    return result
    
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def get_num_days_in_month(month_num, year):
    if is_valid_month_num(month_num):
        if is_leap_year(year) and month_num == 2:
            return 29
        else:
            return days[month_num -1]
    else:
        return None
            
    
def generate_date(start_year, end_year):
    date = [0,0,0]
    date[0] = random.randint(start_year, end_year)
    date[1] = random.randint(1,12)
    date[2] = random.randint(1, get_num_days_in_month(date[1], date[0]))
    return date

