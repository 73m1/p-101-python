import random

response = input("would you like to roll a dice(input 'y' for Yes)")

while response == 'y':
    no = radint(1,6)
    response == ' '
    if(no == 1):
        print("[-----]",end=" ")
        print()
        print("[     ]",end=" ")
        print()
        print("[  0  ]",end=" ")
        print()
        print("[     ]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")
    elif(no == 2):
        print("[-----]",end=" ")
        print()
        print("[0    ]",end=" ")
        print()
        print("[     ]",end=" ")
        print()
        print("[    0]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")
    elif(no == 3):
        print("[-----]",end=" ")
        print()
        print("[0    ]",end=" ")
        print()
        print("[  0  ]",end=" ")
        print()
        print("[    0]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")
    elif(no == 4):
        print("[-----]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[     ]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")    
    elif(no == 5):
        print("[-----]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[  0  ]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")
    elif(no == 6):
        print("[-----]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[0   0]",end=" ")
        print()
        print("[-----]",end=" ")
        print()
        response = input("would you like to roll again(y for Yes, n to exit)")
    if(response == 'n'):
        print("thanks for rollin'")