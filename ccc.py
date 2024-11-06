
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
eleventhdigit = card_str[10]
twelvethdogot = card_str[11]
thirteenthdigit = card_str[12]
fourteenthdigit = card_str[13]
fifteenthdigit = card_str[14]
sixteenthdigit = card_str[15]

# Check Industry Protocol

if firstdigit == "5" and seconddigit == "1":
    print("Mastercard")
    mastercard = True
    visa = False
    americanexpress = False

elif firstdigit == "5" and seconddigit == "5":
    print('Mastercard')
    mastercard = True
    visa = False
    americanexpress = False

elif firstdigit == "4":
    print("Visa")
    visa = True
    mastercard = False
    americanexpress = False

elif firstdigit == "3" and seconddigit == "4":
    print("American Express")
    americanexpress = True
    visa = False
    mastercard = False

elif firstdigit == "3" and seconddigit == "7":
    print("American Express")
    americanexpress = True
    visa = False
    mastercard = False

else:
    print("Not valid with current database")


