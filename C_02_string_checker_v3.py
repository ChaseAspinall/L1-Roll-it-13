
def string_checker(question, valid_ans=["yes", "no"]):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:

            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see instructions? ",)

print("You chose: ", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You chose: ", user_choice)
