#here the shopkeeper can sell the items in the list like
#given input 5 5 4 7 4 1 11
#in this mostly repeated numbers which is highly repeated
#output 7
#and the first output should be print as first output and if anything is not repeated,
#then the first output should be printed as None
#here the output 5

price_list = list(map(int,input().split()))


item_sold_once = None
for each_price in price_list:
    count = price_list.count(each_price)
    if count == 1:
        item_sold_once = each_price
        break
print(item_sold_once)

item_sold_more = None
for each_price in price_list:
    count = price_list.count(each_price)
    if count >= 2:
        item_sold_more = each_price
        break

print(item_sold_more)


