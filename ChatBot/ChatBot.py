from contextlib import contextmanager

@contextmanager
def nested_break():
    class NameNestBreak(Exception):
        pass
    try:
        yield NameNestBreak
    except NameNestBreak:
        pass
 
    
print("Hello! I am a food-ordering chatbot for WaffleInc! Please answer in full sentences.")

#start
while True:
    starta = input("What do you want?: ")
    start = starta.lower()
    if 'i want food' in start or start.strip() =='i want to order food':
        print('Great!')
        break
    elif 'i want' in start:
        print('The ordering comes later, but first...')
        break
    elif 'food' in start:
        print('I\'ll assume you want food.')
        break
    print("Sorry, I didn't understand that. I'm only for ordering food. Just say that you want food.")

    
#ask name
roster = open("roster.txt","r+")
customers = roster.read() 



    
with nested_break() as asknamebreak:
    while True:
        namewhole = input("What's your name?: ")
        namefield = namewhole.lower()
        searchtext = "my name is"
        i = namefield.find(searchtext)
        x = i+len(searchtext)
        name = namefield[x:].strip()
        if "my name is " in namefield: 
            while True:
                confirmname = input("Is " + name.title() + " your name?: ")
                if confirmname.lower() == 'yes' or confirmname.lower() == 'y':
                    print("Great!")
                    raise asknamebreak
                break
        else:
            print("I\'ll need you to say: \"My name is...\". I need to make sure your name isn't \"ambiguous\".")
        print("Let's try this again.")
        
checka = 0        
with open("roster.txt") as f:
    for linea in f:
        if (name.title()) in linea[:len(name)] and checka == 0:
            print("Hello "+ name.title() + "! You've ordered here before. These were your previous orders~")
            print()
            checka = 1
            pass
with open("roster.txt") as fa:        
    for line in fa:
        if (name) in line[:len(name)]:
            print (line[len(name):])
        elif (name.title()) in line[:len(name)]:
            print (line[len(name):])
#menu order
menulist = ["Waffle Fondue", "Waffle Pizza", "Waffle Steak", "Waffle Stack", "Generic Waffle", "Gourmet Waffle", "Waffle Milkshake", "Waffle Sundae"]
menuyesnoa = input("Would you like to see the menu?: ")
menuyesno = menuyesnoa.strip()
if  'yes' in menuyesno.lower():
    print("--------Menu--------")
    for list in menulist:
        print(list)
    print("--------------------")
    
order = []   
amount = 0
orderlistfinal = []
ordernumber = 1
ordernumstr = str(ordernumber)
ordernumstrcheck = (str(0) + ordernumstr)
suffix = "st"
if ordernumstr[-1] == str(1) and str(1) not in ordernumstrcheck[-2]:
    suffix = 'st'
elif ordernumstr[-1] == str(2) and str(1) not in ordernumstrcheck[-2]:
    suffix = 'nd'
elif ordernumstr[-1] == str(3) and str(1) not in ordernumstrcheck[-2]:
    suffix = 'rd'
else:
    suffix = 'th'


print("Please enter your items one by one as it appears on the menu. ")
print("When you have enough, continue with a blank answer.")
print("If you would like to see the menu again, please say so.")
print()



while True:
    while order != '':
        ordera = input('What\'s your ' + str(ordernumber) + str(suffix) + ' order?: ')
        order = ordera.strip()
        if 'menu' in order or 'Menu' in order :
            print("Here's the menu.")
            print("--------Menu--------")
            for list in menulist:
                print(list)
            print("--------------------")
        if order in menulist or order.title() in menulist:
          orderlistfinal.append(order.title())
          print('Your cart: ' + str(orderlistfinal) )
          ordernumber = ordernumber + 1
          ordernumstr = str(ordernumber)
          suffix = "st"
          if ordernumstr[-1] == str(1) and str(1) not in ordernumstrcheck[-2]:
              suffix = 'st'
          elif ordernumstr[-1] == str(2) and str(1) not in ordernumstrcheck[-2]:
              suffix = 'nd'
          elif ordernumstr[-1] == str(3) and str(1) not in ordernumstrcheck[-2]:
              suffix = 'rd'
          else:
              suffix = 'th'
          ordernumstrcheck = (str(0) + ordernumstr)

        elif order != '' and 'menu' not in order and 'Menu' not in order :
            print('This item is not on the menu.')
    
    if len(orderlistfinal)>= 3:
        pass
        ordermorea = input("Would you like to order more?: ")
        ordermore = ordermorea.strip()
        if ordermore.lower() == "yes":
            order = 0
            pass
        else:
            break 
    else:
        print("You must have at least 3 orders for delivery.")
        order = 0
        pass
        
    print('What else would you like?')    
    pass

final = (name.title() + str(orderlistfinal))
roster.write((final)+ "\n")
roster.close()


print()
print('Your order has been saved: ')
print(final)
print('We hope to hear from you again soon, ' + name.title() + ' !')
print()
input("Press 'Enter' to exit")


