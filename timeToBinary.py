import random
random.seed()

# TODO: Add menu/explanation?
# TODO: Add scoring modes?

hour = random.randint(1, 12)
minute = random.randint(1, 59)
second = random.randint(1, 59)
AM_PM = random.randint(0, 1)
AM_PM_str = 'AM' if AM_PM == 0 else 'PM'

while len(str(minute)) != 2:
    minute = '0' + str(minute)
while len(str(second)) != 2:
    second = '0' + str(second)

answer = f"{hour}:{minute}:{second} {AM_PM_str}"

# Convert numbers to binary
hour_bin = format(int(hour), 'b')
minute_bin = format(int(minute), 'b')
second_bin = format(int(second), 'b')

# Adjust Format
while len(hour_bin) != 4:
    hour_bin = '0' + hour_bin

while len(minute_bin) != 6:
    minute_bin = '0' + minute_bin

while len(second_bin) != 6:
    second_bin = '0' + second_bin
# TODO: Prompt should explain output format to the user.
prompt_ = f'''The time is [{AM_PM} {hour_bin} {minute_bin} {second_bin}].
(Answers should be in the format [hh:mm:ss] [am/pm])
What is the time in base-10? \
'''
# Test the user:

time_guess = input(prompt_)

# Results
if time_guess.lower() == answer.lower():
    response = f'''You're Right!

The correct Time was "{answer}".
'''
else:
    response = f'''Not Quite...

The Correct Time was "{answer}".
Your Guess was "{time_guess}".
'''
print(response)

