def Caffy(): 
  print("I'm Caffy, the coffee bot. I exist to make sure no human goes uncaffeinated.")

Caffy()

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
    get_size()
size = get_size()
print(size)