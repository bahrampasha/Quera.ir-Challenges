stones = {'space':'blue',
          'mind':'yellow',
          'reality':'red',
          'power':'purple',
          'time':'green',
          'soul':'orange',
          }


while True:
    Stone_name  = input("What color is this, Human?\n")
    if  Stone_name.isalpha(): 
        Stone_name.strip().lower()
        print(Stone_name)
        if Stone_name != 'end' :
            if Stone_name in stones:
                print(f"The color of '{Stone_name}' stone is {stones[Stone_name]}")
            else:
                print("Appologize My Lord, Would you Please type it again?")

        else:
            break