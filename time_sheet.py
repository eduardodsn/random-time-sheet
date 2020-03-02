import pandas as pd
import datetime
from random import *

def generate_data(hour, minute):
    return datetime.time(hour=hour, minute=minute)


def generate_entry(qnt_days):
    for i in range(qnt_days):
        hour = randint(7, 8)

        if hour == 7:
            minute = randint(15, 59)
        else:
            minute = randint(0, 6)
        
        generated_hour = generate_data(hour, minute)
        entry_list.append(generated_hour)
        

def generate_exit(qnt_days, working_time):
    for i in range(qnt_days):
        hour = entry_list[i].hour + working_time
        minute = entry_list[i].minute + (randint(0, 6))
        while minute > 59:
            minute = minute - 1

        generated_hour = generate_data(hour, minute)
        exit_list.append(generated_hour)


qnt_days = int(input('Quantity of days: '))
working_time = int(input('Working time: '))
entry_list = []
exit_list = []

generate_entry(qnt_days)
generate_exit(qnt_days, working_time)

df = pd.DataFrame(index = range(1, qnt_days + 1))
df['Entry'] = entry_list
df['Exit'] = exit_list

print(df)
