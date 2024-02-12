
def user_choice():
    acceptable_input_range = range(0, 10)
    within_range = False
    choice = 'wrong input'
    while not choice.isdigit() or not within_range:
        choice = input("Please enter a number between (0-10) ::")
        if not choice.isdigit():
            print("Please enter a  valid number ")
        if choice.isdigit():
            if int(choice) in acceptable_input_range:
                within_range = True
    return int(choice)


print(user_choice())
