a=["Hanok","Adharsh","Ani","Amit"]
# print(a[1:3])
password= ["hanokisapro","1234","0987","4567"]
database={"Hanok":"hanokisapro","Adharsh":"1234","Ani":"0987","Amit":"4567"}#in curly brackets and if key avvilable than can print the value
x=input("Enter username: ")
y=input("Enter password: ")
# print(database["Hanok"])

if x in database:
    if database[x] == y:
        print ("Welcome")

    else:
        print("Access denied")
else:
    print("Wrong information. Please try again")