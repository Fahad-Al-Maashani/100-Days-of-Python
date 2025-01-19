print ("Welocme to the tip calculator! ") 
bill =float (input ("What was the total bill ? "))
tip=int(input("How much tip would you like to give ? 10,12, or 15? 12 ")) 
people = int(input ("How many people to split the bill ")) 
perc= tip/100 
total_perc = bill *perc
total= total_perc+bill 
per_person= total/people
print (round (per_person,3))

