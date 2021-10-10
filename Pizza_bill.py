print("Welcome To 🍕Pizza Deliveries! ")
size=input("What size Pizza 🍪🍕 do you want? S, M, L -> ")
add_pepperoni =input("Do you want pepperoni? Y or N -> ")


bill=0
if size =="S":
    bill +=15
elif size =="M":
    bill +=20
else:
    bill +=25

if add_pepperoni =="Y":
    pepperoni_size=input("What size Pepperoi you want? S or L -> ")
    if size =="S":
        bill +=2
    else:
        bill +=3
        
extra_cheese= input("Do you want extra cheese? Y or N -> ")
if extra_cheese =="Y":
    bill +=1

print(F"🍪🍕your final bill is: ${bill}.")
