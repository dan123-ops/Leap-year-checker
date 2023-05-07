user_year = int(input("Please enter a year: "))
# Request user input
user_year_check = int(input(f'How many years after {user_year} would you like to check for?: '))
# request user input including previous user input in this question


# The 'for' loop below initiates a check looking at years from the first year input...
# ....by the amount the user would like to check from the second input

for i in range(0, user_year_check):
    if (user_year + i) % 100 == 0 and (user_year + i) % 400 == 0:
        print(f'{user_year + i} is a leap year')
# This will check if the year is divisible by 100 and 400, hence remainder 0

    elif (user_year + i) % 100 != 0 and (user_year + i) % 4 == 0:
        print(f'<<<{user_year + i} is a leap year>>>')
# 2nd check for if the year is not divisible by 100 and is divisible by 4, hence remainder 0 again

    else:
        print(f'{user_year + i} is not a leap year')
# Final check will be initiated if the 2 previous checks were not satisfied
