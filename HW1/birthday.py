# birthday.py
# Bowen Zhang
# bz896
# Homework 01

import mydate

print("How many times should I run the simulation?")
trials = input()
print("How many birthdays should I generate per trial?")
entries = input()

birthdays = []
count = 0 # count the number of trials which have duplicate birthdays

for x in range(int(trials)):
    for y in range(int(entries)):
        birthdays.append(mydate.generate_date(1900, 2018))
    new_birthdays = mydate.remove_years(birthdays)
    #print(new_birthdays)
    duplicate = [x for n, x in enumerate(new_birthdays) if x in new_birthdays[:n]] # this line is taken from stackoverflow regarding how to make a new list of duplicates
    if len(duplicate) == 0:
        print("Trial #" + str(x+1) + ": No dates are the same.")
    else:
        count += 1
        if len(duplicate) > 1:
            print("Trial #" + str(x+1) + ": " + str(len(duplicate)) + " dates occur more than once! (" + mydate.dates_to_strings(duplicate) + ")")
        else:     
            print("Trial #" + str(x+1) + ": " + str(len(duplicate)) + " date occurs more than once! (" + mydate.dates_to_strings(duplicate) + ")")
    birthdays.clear()

print()
print("Results:")
print("=====")
print(f"Out of {trials} trials, {count} had dates that were repeated.")
print(f"We can conclude that you have a {count/int(trials):.2%} chance of sharing a birthday with someone if you are in a group of {entries} people.")