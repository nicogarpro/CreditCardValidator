# CURRENTLY UNABLE TO RECOGNIZE CARDS
# CURRENTLY DEFECTIVE
# Ask for an input

card = input("Please type card number \n")

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
twelvethdigot = card_str[11]
thirteenthdigit = card_str[12]
fourteenthdigit = card_str[13]
fifteenthdigit = card_str[14]
sixteenthdigit = card_str[15]

# Also get every digit not to be a string

numone = int(firstdigit)
numtwo = int(seconddigit)
numthree = int(thirddigit)
numfour = int(fourthdigit)
numfive = int(fifthdigit)
numsix = int(sixthdigit)
numseven = int(seventhdigit)
numeight = int(eighthdigit)
numnine = int(ninthdigit)
numten = int(tenthdigit)
numeleven = int(eleventhdigit)
numtwelve = int(twelvethdigot)
numthirteen = int(thirteenthdigit)
numfourteen = int(fourteenthdigit)
numfifteen = int(fifteenthdigit)
numsixteen = int(sixteenthdigit)

# Luth Algorithm

verififteen = (numfifteen + numfifteen)
verithirteen = (numthirteen + numthirteen)
verieleven = (numeleven + numeleven)
verinine = (numnine + numnine)
veriseven = (numseven + numseven)
verifive = (numfive + numfive)
verithree = (numthree + numthree)
verione = (numone + numone)

verinumber = (verione + numtwo + verithree + numfour + verifive + numsix + veriseven + numeight + verinine + numten + verieleven + numtwelve + verithirteen + numfourteen + verififteen + numsixteen)

veridivided = (verinumber / 10)

print(verinumber, ", ", veridivided)