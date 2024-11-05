

# Ask for an input

card = input("Please type card number")

# Convert number into a string

card_str = str(card)

firstdigit = card_str[0]
seconddigit = card_str[1]
thirddigit = card_str[2]
fourthdigit = card_str[3]
fifthdigit = card_str[4]
sixthdigit = card_str[5]
seventhdigit = card_str[6]
eighthdigit = card_str[7]
ninthdigit = card_str[8]
tenthdigit = card_str[9]



# Check Industry Protocol

if firstdigit == "5" and seconddigit == "1":
    print("Mastercard")
    mastercard = True

elif firstdigit == "5" and seconddigit == "5":
    print('Mastercard')
    mastercard = True

else:
    mastercard = False