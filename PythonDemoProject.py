print("Sonya's Demographics Project")
print("Welcome!")
print()
                # name
name_min = 2
name_max = 50
name_count = 0
christian_name = 'What is first your name?'
surname = 'What is last your name? '
name_too_short = "Name must be at lease 2 characters. "
name_too_long = "Name can be a maximum of 50 characters. "
while name_min < name_max:
    first_name = input(christian_name).capitalize()
    if len(first_name) < 2:
        print(name_too_short)
    elif len(first_name) > 50:
        print(name_too_long)
    else:
        break
while name_min < name_max:
    last_name = input(surname).capitalize()
    if len(last_name) < 2:
        print(name_too_short)
    elif len(last_name) > 50:
        print(name_too_long)
    else:
        print("Name looks good")
        break
print('Welcome! ' + first_name + ', ' + last_name)

                    # today's year import
from datetime import date
this_year = date.today().year
today = date.today()
print(f'Today is {today}')
                    # DOB
try:
    birth_year = int(input('Birth Year: '))
    age = this_year - birth_year
    print(age)
except ValueError:
    print("Invalid value. Please enter numbers only. ")
    while True:
        birth_year = int(input('Birth Year: '))
        age = this_year - birth_year
        print(age)
        break
new_age = age + 7
print(f'In seven years you will be {new_age}')

                    # weight conversion
weight = int(input("What is your current weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    from converters import lbs_to_kg
    print(f"you are {int(lbs_to_kg(weight))} kilos")
else:
    print(f"you are {weight} kilos")

                 #Emoji call
def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ":)": "\N{grinning face}",
        ":*": "\U0001F48B",
        "<)": "\U0001F618",
        "<3": "\U0001F496",
        "><": "\U0001F921",
        ":(": "\U0001F622",
        "*)": "\U0001F609"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


text = input("What is your favorite emoji? ")
print(emoji_converter(text))

                    # favorite color
fav_color = input('What is your favorite color? ')
print(f'{first_name}, {last_name} is {age} as at {this_year}, and likes the color {fav_color} and the emoji {emoji_converter(text)}.')

                    # thank you email formatting
email = '''
        Hi There,
        
        Thank you for your participation.
        
        Regards,
        Support

'''
print(email)
