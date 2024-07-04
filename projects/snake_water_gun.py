import random

computer_keys = random.choice([1, -1, 0])
keys_and_values = {
    's': 1,
    'w': -1,
    'g': 0,
}
get_choice = input("Enter your Choice 's,w,g' :")
get_keys = keys_and_values[get_choice]
# print(get_keys)

get_name_values = {
    1: "snake",
    -1: "water",
    0: "gun"
}

print(f"You chose >>> {get_name_values[get_keys]} \nComputer chose >>> {
      get_name_values[computer_keys]}")


def main_scenario():
    if (computer_keys == get_keys):
        print("Its a Draw")
    else:
        if (computer_keys == -1 and get_keys == 1):
            print("You win!")
        elif (computer_keys == -1 and get_keys == 0):
            print("You lose!")
        elif (computer_keys == 1 and get_keys == -1):
            print("You lose!")
        elif (computer_keys == 1 and get_keys == 0):
            print("You win!")
        elif (computer_keys == 0 and get_keys == -1):
            print("You win!")
        elif (computer_keys == 0 and get_keys == 1):
            print("You lose!")
        else:
            print("Something Went Wrong.")


main_scenario()

# shortened method


# def main_scenario():
#     if (computer_keys == get_keys):
#         print("Its a Draw")
#     else:
#         if ((computer_keys - get_keys) == -1 or (computer_keys - get_keys) == 2):
#             print("You lose")
#         else:
#             print("You win!")


# main_scenario()
