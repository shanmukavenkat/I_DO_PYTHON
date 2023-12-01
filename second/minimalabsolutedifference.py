#Test Case: If the given N  7 1 5
#The absolute difference between the heights of any two different
#pyramids are
#Pyramid-A Pyramid-B Diff
#7         1           6
#7         5           2
#1         5           4
#From the above table, the minimum absolute difference is 2.
#The output should be 2.




heights = list(map(int,input().split()))
list_a = sorted(heights,reverse=True)
def minimal_diff_heights(list_a):
    list_b = []
    for i in range(len(list_a)):
        for j in range(i+1,len(list_a)):
            min_h = list_a[i] - list_a[j]
            list_b.append(min_h)
    print(min(list_b))
minimal_diff_heights(list_a)