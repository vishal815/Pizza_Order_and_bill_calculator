print("Welcome To 🍕Pizza Deliveries! ")


while(True):
    size_lower = input("What size Pizza 🍪🍕 do you want? S, M, L -> ").lower()
    if size_lower != 's' and size_lower != 'm' and size_lower != 'l':
        print("Your input is invalid. Please enter a valid input.")
        continue
    else:
        break

while(True):
    add_pepperoni_lower = input("Do you want pepperoni? Y or N -> ").lower()
    if add_pepperoni_lower != 'y' and add_pepperoni_lower != 'n':
        print("Your input is invalid. Please enter a valid input.")
        continue
    else:
        break


bill = 0
if size_lower == "s":
    bill += 15
elif size_lower == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni_lower == "y":

    while(True):
        pepperoni_size = input(
            "What size Pepperoi you want? S or L -> ").lower()
        if pepperoni_size != 's' and pepperoni_size != 'l':
            print("Your input is invalid. Please enter a valid input.")
            continue
        else:
            break

    if size_lower == "s":
        bill += 2
    else:
        bill += 3

while(True):
    extra_cheese_lower = input("Do you want extra cheese? Y or N -> ").lower()
    if extra_cheese_lower != 'y' and extra_cheese_lower != 'n':
        print("Your input is invalid. Please enter a valid input.")
    else:
        break


if extra_cheese_lower == "y":
    bill += 1

print(F"🍪🍕your final bill is: ${bill}.")
