#If the given test cases T  2
#Test Case 1 If the given X  300 , results  ADDAADDDAADADA
#The total prize pool is 30000 as 100 * X .
#Among 14 matches, 7 matches won by Amanda and 7 matches are draw. So, Amanda is a champion.
#So, The Mary Kom is a loser. She gets 40 * X , i.e 12000.
#The output should be 12000.
#Test Case 2 If the given X  400 , results  AMMMMAMDMADMAD
#The total prize pool is 40000 as 100 * X .
#Among 14 matches, Amanda has won 4 matches, Mary Kom has won 7 matches and 3 matches are draw. So, Mary Kom is a
#champion.
#So, The Mary Kom is a winner. She gets 60 * X , i.e 24000.
#The output should be 24000.
#Sample Input 1
#2
#300
#ADDAADDDAADADA
#400
#AMMMMAMDMADMAD
#Sample Output 1
#12000
#24000

num = int(input())

for i in range(num):
    prize_m = int(input())*100
    line = input()
    Amanda = 0
    Mary = 0
    Draw = 0
    for j in line:
        if j == "A":
            Amanda += 1
        elif j == "M":
            Mary += 1
        else:
            Draw += 1
    if Mary > Amanda:
        prize = prize_m/100*60
        print(prize)
    elif Mary == Amanda:
        prize = prize_m/100*55
        print(prize)
    else:
        prize = prize_m / 100 * 40
        print(prize)