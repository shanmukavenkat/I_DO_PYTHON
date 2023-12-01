# MrStark is facing the north. Peter is in trouble, and he is facing the
# south. Stark being his mentor will protect him as soon as he sees that
# Peter is in trouble.
# Stark's suit is programmed to rotate automatically in the direction of
# most enemies. By analyzing the direction in which most enemies are
# heading, the suit provides you with the next set of suit instructions in
# the form of a string S.
# When Stark faces south, he ignores the rest of his suit instructions
# and immediately goes to rescue Peter.
# Write a program that reads the set of suit instructions S and
# determines whether Stark will be able to save Peter.

all_directions = ["north", "east", "south", "west"]

test_cases = int(input())
for i in range(test_cases):
    directions = input()  ##RLRLLLR

    initial_direction = 0
    final_result = ""
    for each_direction in directions:
        if each_direction == "R":
            initial_direction += 1
            check_direction = all_directions[initial_direction]
            if check_direction == "south":
                final_result = "YES"
                break
            else:
                final_result = "NO"
        if each_direction == "L":

            initial_direction -= 1
            check_direction = all_directions[initial_direction]
            if check_direction == "south":
                final_result = "YES"
                break
            else:
                final_result = "NO"
    print(final_result)
