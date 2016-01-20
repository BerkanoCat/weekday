def get_user_input():
    user_input = input("Please input desired date in the following format: MM/DD/YYYY:  ")
    return user_input.split("/")
    
    
def parse_year(year):
    # we need the split the year up into two seperate two-digit numbers: the century, and the
    # last two digits. They're both important to the overall equation.
    year = str(year)
    return [year[0:2], year[2:4]]
    
    
def is_leap_year(year):
    # This simply determines whether or not the year is a leap year, which has a slight
    # bearing on the final calculation.
    century = int(year[0])
    last_two = int(year[1])
    
    if last_two % 4 != 0:
        return False
    elif century % 4 == 0 and last_two == 0:
        return True
    elif last_two == 0:
        return False
    else:
        return True
    
    
def find_year_code(year):
    century = year[0]
    last_two = year[1]
    # Here we determine whether or not to modify the year code based on what century we're
    # working with.  In the 21st century, no modifcation is made.
    century = int(century)
    if century % 4 == 0:
        year_code_default = 0
    if century % 4 == 3:
        year_code_default = 1
    if century % 4 == 2:
        year_code_default = 3
    if century % 4 == 1:
        year_code_default = 5
    
    # we convert last_two into an integer, add the quotient of last_two and 4, and then find
    # the remainder of the new number and 7 for our year code.
    if last_two[0] == "0":
        last_two = last_two[1]
    last_two = int(last_two)
    last_two += last_two // 4
    # last_two += last_two / 4  USE THIS LINE INSTEAD OF THE PREVIOUS IF USING PYTHON2
    year_code = last_two % 7
    return (year_code + year_code_default) % 7
    
    
def get_weekday():
    # this function takes the user input and performs the final calculation. This is the
    # primary function of this module. First, we've got a few variables to declare.
    query = get_user_input()
    month = query[0]
    date = int(query[1])
    year = parse_year(int(query[2]))
    
    month_codes = {"01": 6, "02": 2, "03": 2, "04": 5, "05": 0, "06": 3, "07": 5, "08": 1, "09": 4, "10": 6, "11": 2, "12": 4}
    weekday_codes = {"0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday"}
    
    # find year code
    year_code = find_year_code(year)
    
    # and month code
    month_code = 0
    if is_leap_year(year) and month == "01":
        month_code = 5
    elif is_leap_year(year) and month == "02":
        month_code = 1
    else:
        month_code = month_codes[month]
        
    # and now, the moment of truth!
    total = str((year_code + month_code + date) % 7)
    weekday = weekday_codes[total]
    return weekday