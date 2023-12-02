#You are given the arrival and departure times of some trains in 24-hour format.
# Your task is to determine the minimum number of platforms needed at a railway station to accommodate all trains arriving and
# departing (i.e. ensuring that no two trains overlap at a single platform and no train is left waiting).

#All trains arrive and depart on the same day, with distinct arrival and departure times.
# To prevent conflicts, separate platforms are needed for trains whose arrival overlaps with
# the departure of another train on the same platform.

#Write a program that reads the arrival and departure times of the trains in 24-hour format
# and prints the minimum number of platforms needed at a railway station to accommodate all trains.


#To solve this problem, we will follow these steps:

#1 Read the input arrival and departure times and convert them into lists.
#2 Sort the arrival and departure times.
#3 Calculate the minimum number of platforms required by comparing the arrival and departure times.
#4 Print the result.


#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 1: Read Input and Convert to Lists
#First, we need to read the input arrival and departure times and convert them into lists.
#We can use the input() function to read the input and split() to convert the input into a list.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 2: Sort Arrival and Departure Times
#Next, we need to sort the arrival and departure times. We can use the sort() function to sort the lists.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 3: Calculate Minimum Platforms Required
#Now, we will calculate the minimum number of platforms required by comparing the arrival and departure times.
# We will use two pointers i and j to iterate through the arrival and departure times lists.
# We will also use two variables platforms_required and max_platforms_required to keep track of
# the current number of platforms required and the maximum number of platforms required so far.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 4: Print the Result
#Finally, we will print the result, which is the value of max_platforms_required.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

def get_number_of_platforms_required(train_arrival_times_list, train_depature_times_list, total_no_of_trains):
    train_arrival_times_list.sort()
    train_depature_times_list.sort()

    platforms_required = 1
    max_platforms_required = 1
    i = 1
    j = 0

    while ((i < total_no_of_trains) and (j < total_no_of_trains)):
        if (train_arrival_times_list[i] <= train_depature_times_list[j]):
            platforms_required += 1
            i += 1
        else:
            platforms_required -= 1
            j += 1

        if (platforms_required > max_platforms_required):
            max_platforms_required = platforms_required

    return max_platforms_required

def main():
    train_arrival_times_list = input().split()
    train_depature_times_list = input().split()
    total_no_of_trains= len(train_arrival_times_list)
    result = get_number_of_platforms_required(train_arrival_times_list, train_depature_times_list, total_no_of_trains)
    print(result)

main()

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#a = list(map(int,input().split()))
#a.sort()
#d = list(map(int,input().split()))
#d.sort()
#listing = []
#for i in range(len(a)):
#    if (i == 0):
#       listing.append(d[i])
#    else:
#        for j in listing:
#            if a[i] > j:
#                listing.remove(j)
#                listing.append(d[i])
#                break
#            else:
#                listing.append(d[i])
#                break

#print(len(listing))
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
