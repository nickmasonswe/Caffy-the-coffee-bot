def Caffy(): 
  print("I'm Caffy, the coffee bot. I exist to make sure no human goes uncaffeinated. \n")
  size = get_size()  
  drink_type = get_drink_type()

  print("Alright, that\'s a {} {}".format(size, drink_type))
  name = get_name()
  print("OK hum-- I mean, {}".format(name) + ", your drink will be ready soon")


def get_size():
  response = input('What size will your beverage be, human? \n[1] Big \n[2] Massive \n[3] Ridonkulous \n>')
  if response == '1':
    return 'Big'
  elif response == '2':
    return 'Massive'
  elif response == '3':
    return 'Ridonkulous'
  else: 
    print("Pick one of our sizes or leave the establishment! \n... \n...")
    return get_size()

def get_drink_type():
  response = input("What type of drink will satisfy your caffiene withdrawl today? \n [1] Drip Coffee \n [2] Latte \n [3] Matcha \n>")
  if response == '1':
    return 'Coffee!'
  elif response == '2':
    return 'Latte, understood.'
  elif response == '3':
    return 'Matcha complete with brewing ceremony!'
  else:
    print("Pick one of our drinks or leave the establishment! \n... \n...")
    return get_drink_type()
def get_name():
  response = input("What's your name, human? \n ")
  return response

Caffy()