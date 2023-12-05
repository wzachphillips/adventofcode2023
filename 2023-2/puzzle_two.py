'''Advent of code 2023 Problem 2'''
import re
import pandas as pd

with open("2023-2/input.txt","r",encoding='utf-8') as example:
    INPUT = example.read().split('\n')

def get_max_color_value(game_string: str, color_name: str) -> int:
    '''gets maximum color values and returns dictionary
       with corresponding values by color'''
    re_pattern = f'(\d+)(?: {color_name})'
    values = re.findall(re_pattern,game_string)
    numbers = map(int,values)
    return max(numbers)

value_list = []

for line in INPUT:

    row = []

    row.append(re.findall('Game (\d+)',line)[0])
    row.append(get_max_color_value(line,'red'))
    row.append(get_max_color_value(line,'green'))
    row.append(get_max_color_value(line,'blue'))
    value_list.append(row)


print(value_list)
columns = ['GameID','MaxRed','MaxGreen','MaxBlue']
df = pd.DataFrame.from_records(value_list,columns=columns)

def determine_valid(max_red,max_green,max_blue):
    '''Determines the value of each max color is
       passing then returns if the row passes'''
    truth_table = []
    truth_table.append(max_red <= 12)
    truth_table.append(max_green <= 13)
    truth_table.append(max_blue <= 14)

    for result in truth_table:
        if result is False:
            valid = False
            break

        valid = True

    return valid

df['valid'] = df.apply(lambda x: determine_valid(x.MaxRed, x.MaxGreen, x.MaxBlue), axis = 1)
df['MinViable'] = df['MaxRed'] * df['MaxGreen'] * df['MaxBlue']

print(df.head())

print(f'The Sum of Valid ID\'s is: {df.loc[df["valid"] == True, "GameID"].astype(int).sum()}')
print(f'The Sum of Powers for Minimum Viable Configurations is {df["MinViable"].astype(int).sum()}')
