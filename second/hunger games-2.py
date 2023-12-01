#here the player who gets the last chocolate is the winner,
#here the player distribution is in a circle
#here the ist integer is the number of players and the second integer is the number of chocolates
#here the third integer is the starting player
#let us take input as 2
#2 inputs should be given and three integers should be given in a single line
#3 5 1
#3 5 2
#here the output should be 3 and 2


number = int(input())

for i in range(number):
    line_n = list(map(int,input().split()))
    players = line_n[0]
    chocolates = line_n[1]
    starting_player = line_n[2]
    for j in range(chocolates-1):
        if starting_player == players:
            starting_player = 0+1
        else:
            starting_player += 1
    print(starting_player)


