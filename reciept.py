ans='y'
total=0
item=[]
price=[]
n=1
while ans=='y':
    i=input("enter item names bought:")
    item.append(i)
    p=int(input("enter price:"))
    price.append(p)
    ans=input("want to add more? y/n")
    total+=p
    n+=1
    
print('*'*50)
print("WELCOME TO OUR STORE")
print("*"*50)
print("ITEMS""               ""PRICE")
for i in range(n):
    print(i+1,".",item[i],"            ",price[i])
print("#"*50)
print("your total amount to be payed :",total)
print('*'*50)
print("THANK YOU FOR SHOPPING")
    



