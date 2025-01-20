#This python program simulate how rollercoaster service provide can show a service prices to their customer
#print  the welcome statement
print("Welcome to the rollercoaster game !")
#prompt the from customer the input of her or he height in cm
height = int(input("Please customer enter your height ?"))
#check conditional statement if height > 12o or not for eligibility purpose
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age"))
  #check the age of customer and print exact price according to the client age
    if age>18:
            print("Pay $12")
      #Check if  customer need a photo taken or not that will add additional price to the overall bill
            photo=  (input("Would you like to have a photo taken"))
            if photo == "Yes":
                print ("Pay $ 3 more")
                print ("Total Bill is $15")
            else:
                print("Total bill is $ 12 only")
    #This go the same before condition statement age>18
    elif age >=12 and age <=18:
            print("Pay $7")
            photo = (input("Would you like to have a photo taken"))
            if photo == "Yes":
                print("Pay $ 3 more")
                print("Total Bill is $10")
            else:
                print("Total Bill is $7")
    elif age <12:
            print("pay $ 5")
            photo = (input("Would you like to have a photo taken"))
            if photo == "Yes":
                print("Pay $ 3 more")
                print("Total Bill is $8")
            else:
 
                print("Total Bill is $ 5")
#in case heightn < 120 cm the customer wil be not eligible to use the rollercoaster. 
else:
    print("You cant ride the rollercoaster")
