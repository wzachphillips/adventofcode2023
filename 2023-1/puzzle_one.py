'''Advent of code 2023 Problem 1'''
import re
import tabulate

with open("2023-1/input.txt","r",encoding='utf-8') as example:
    INPUT = example.read().split('\n')

#Use for each line to get answer to problem 1
def get_calibration_value(input_string:str) -> int:
    '''Get's malformed lined and returns valid calibration value'''
    digit_list = re.findall('\d',input_string)
    print(digit_list)
    value_list = []
    value_list.append(digit_list[0])
    value_list.append(digit_list[-1])
    merged_list = []
    merged_list.append(''.join(value_list))
    merged_list = [int(i) for i in merged_list]
    return merged_list[0]

#Problem 2
def build_subtituion_regex(input_list: list) -> str:
    '''takes a list of valid values and returns OR regex'''
    re_pattern = ''

    for item in input_list:
        re_pattern = re_pattern + item + '|'
    re_pattern = re_pattern[0:-1]
    re_pattern = '(' + re_pattern + ')'

    return re_pattern

def replace_line_values(sub_list: list,
                          replace_value_list: list,
                          input_string:str) -> str:
    '''Replace list value in str with relative replacement value'''
    subsitution_list = sub_list
    replace_list = replace_value_list

    replacement_dict = {}
    i = 0
    while i < len(subsitution_list):
        replacement_dict[subsitution_list[i]] = replace_list[i]
        i += 1

    re_pattern = build_subtituion_regex(subsitution_list)

    replace_words = re.findall(re_pattern,input_string)
    print(replace_words)
    replaced_string = input_string
    for word in replace_words:
        replaced_string = replaced_string.replace(word,replacement_dict[word])
    
    print(replaced_string)

    return replaced_string

#Added to see organized output of transformations
debug_list = []

line_values = []

#core replacement values
substitution_list = ['one','two','three','four','five',
                     'six','seven','eight','nine']
replace_value_list = ['1','2','3','4','5','6','7','8','9']

#overlapping errors. Resolve this first.
fix_list = ['oneight','twone','eighthree','threeight','eightwo',
            'nineight','sevenine','fiveight']
fix_replace_list = ['oneeight','twoone','eightthree','threeeight',
                    'eighttwo','nineeight','sevennine','fiveeight']

for line in INPUT:
    line_list = []
    line_list.append(line)
    try:
        fix_line = replace_line_values(fix_list,fix_replace_list,line)
        line_list.append(fix_line)
        sub_value = replace_line_values(substitution_list,
                                          replace_value_list,
                                          fix_line)
        line_list.append(sub_value)
        calibration_value = get_calibration_value(sub_value)
        line_list.append(calibration_value)
        line_values.append(calibration_value)
        debug_list.append(line_list)

    except Exception as e:
        print(e)

print(tabulate.tabulate(debug_list))
print(sum(line_values))
