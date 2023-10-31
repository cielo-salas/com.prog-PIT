
print("----**************************----")
print("\nHello Kids Let's Combine Colors")

print("\n****Select your primary color****")
color1 = int(input('\nPress 1 for RED'
                   '\nPress 2 for YELLOW'
                   '\nPress 3 for BLUE '
                   '\nENTER HERE:'))
if color1 == 1:
    print("You have selected RED")
elif color1 == 2:
    print("You have selected YELLOW")
elif color1 == 3:
    print("You have selected BLUE")
else:
    print("The input is invalid,refer to the choices.")

print("------------------------------------------------------------")
print("*****NOW LETS PROCEED ON SELECTING THE SECONDARY COLORS*****")
print("\n*****Select your secondary color*****")
color2 = int(input("\nPress 5 for GREEN"
                   "\nPress 6 for ORANGE "
                   "\nPress 7 for PURPLE"
                   "\nENTER HERE:"))
if color2 == 5:
    print("You have selected GREEN ")
elif color2 == 6:
    print("You have selected ORANGE ")
elif color2 == 7:
    print("You have selected PURPLE ")
else:
    print("The input is invalid,refer to the choices.")

print('---------------------------------------------------')
print("*****THE RESULT OF THE COLORS YOU HAVE CHOSEN*****"
      "\nTHE TERTIARY RESULT IS:")
inputs = color1 * color2

if inputs == 5:
    print("YELLOW")
elif inputs == 6:
    print("VERMILION")
elif inputs == 7:
    print("MAGENTA/RED-VIOLET")
elif inputs == 10:
    print("YELLOW-GREEN")
elif inputs == 12:
    print("AMBER")
elif inputs == 14:
    print("BROWN")
elif inputs == 15:
    print("TEAL")
elif inputs == 18:
    print("REDDISH-BROWN OF BURNT SIENNA")
elif inputs == 21:
    print("BLUE-VIOLET")
else:
    print("Can't read the input.")
