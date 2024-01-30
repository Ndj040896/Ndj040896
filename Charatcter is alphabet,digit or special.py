# Program to check character is Alphabet Digit or Special Character:

ch = input(" Enter the Character : ")

if(ch.isalpha()):
    print(" Given Character ", ch, "is an Alphabet")
elif(ch.isdigit()):
    print(" Given Character ", ch, "is a Digit")
else:
    print(" Given Character ", ch, "is a Special Character")
