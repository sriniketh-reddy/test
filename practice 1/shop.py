sal = int(input())
shop = list(map(int,input().split()))
print("Total Shopping amount: ",sum(shop))
print("Percentage of shopping expenditure: ",((sum(shop))/sal*100))