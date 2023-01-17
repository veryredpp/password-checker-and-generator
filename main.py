import random
import sys
import pick
import time
import os

keyboardRows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
allowedKeys = "qwertyuiopasdfghjklzxcvbnm" + "1234567890" + "!$%^&*()-_=+"
allowedKeys = list(allowedKeys)

allowedKeysPlusCapitals = "qwertyuiopasdfghjklzxcvbnm" + "1234567890" + "!$%^&*()-_=+" + "QWERTYUIOPASDFGHJKLZXCVBNM"
allowedKeysPlusCapitals = list(allowedKeysPlusCapitals)


def showmenu():
    title = "Password Checker and Generator"
    options = ["Check Password", "Generate Password", "Quit"] #Will be referred to as 0,1,2 respectively from here on
    option, index = pick.pick(options, title, indicator="=>")
    print(option)
    print(index)
    return index

def calculatePoints(password: str):
    
    points = len(password)
    
    #Point addition
    passwordContainsOneUppercase = any(letter.isupper() for letter in password)
    if passwordContainsOneUppercase:
        points += 5
            
    passwordContainsOneLowercase = any(letter.islower() for letter in password)
    if passwordContainsOneLowercase:
        points += 5
            
    passwordContainsOneDigit = any(letter.isdigit() for letter in password)
    if passwordContainsOneDigit:
        points += 5
            
    passwordContainsOneSymbol = any(letter in list("!$%^&*()-_=+") for letter in password)
    if passwordContainsOneSymbol:
        points += 5
                
    if passwordContainsOneUppercase and passwordContainsOneLowercase and passwordContainsOneDigit and passwordContainsOneSymbol:
        points += 10
            
    #Point deduction
            
    if password.isalpha():
        points -= 5
            
    if password.isdigit():
        points -= 5
                
    if all(letter in list("!$%^&*()-_=+") for letter in password):
        points -= 5
            
            
    badCombos = []
            
    for row in keyboardRows:
                
        for i in range(len(row)-2):
                    
            badCombos.append(row[i:i+3])
                    
            
    formattedPassword = password.strip().lower()
    for badCombo in badCombos:
        count = formattedPassword.count(badCombo)
        points -= 5 * count
        
    return points


while True:
    choice = showmenu()
    os.system("cls")
    
    if choice == 0:
        password = input("Enter Password: ")
        
        check1 = 8 > len(password) or len(password) > 24
        if check1:
            print(f"Password provided is {len(password)} characters long. It should be 8-24 character long.")
        
        check2 = not(set(password.lower()) <= set(allowedKeys))
        if check2:
            print(f"Incorrect symbols used in password.")
        
        if check1 or check2:
            time.sleep(2)
               
        else:
            points = calculatePoints(password)
            
            print(f"Password Score: {points}")
            
            if points <= 0:
                print("Password Strength: Weak")
            elif points > 20:
                print("Password Strength: Strong")
            else:
                print("Password Strength: Medium")
  
            time.sleep(5)
            
             
             
    
    elif choice == 1:
        password = "y" #just a random string to initiate the loop
        
        while not(calculatePoints(password) > 20):
            length = random.randint(8,12)
            
            shuffledAllowedKeys = allowedKeysPlusCapitals.copy()
            random.shuffle(shuffledAllowedKeys) #for good measure
            
            password = [random.choice(shuffledAllowedKeys) for _ in range(length)]
            password = "".join(password)
        
        print(f"Generated Password: {password}")
        print(f"Generated Password Score: {calculatePoints(password)}")
        print(f"Generated Password Strength: Strong")
        time.sleep(10)
    
    elif choice == 2:
        text = "Quitting..."
        loop = range(1, len(text) + 1)
        
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        
        for idx in reversed(loop):
            print(text[:idx])
            time.sleep(.10)
            print(LINE_UP, end=LINE_CLEAR)
        sys.exit()
