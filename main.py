import time


class ItemsOfTime:
    hour = 0
    minute = 59
    second = 0


item = ItemsOfTime()


def start_to_count():
    seconds_counter = 0
    minute_number = item.minute
    while seconds_counter != 60:
      time.sleep(1)
        seconds_counter += 1
        item.second = seconds_counter
        print("{a} hours, {b} minutes {c} seconds".format(a=item.hour, b=item.minute, c=item.second))
        if seconds_counter == 60:
            minute_number += 1
            item.minute = minute_number

        if item.minute == 60:
            item.hour += 1
            item.minute = 0

choice = input("Start the timer: Y/n")

if choice == 'Y':
    flag = True
    while flag:
        start_to_count()

else:
    exit(0)
