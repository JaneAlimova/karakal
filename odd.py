from datetime import datetime

odds = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
         42, 44, 46, 48, 50, 52, 54, 56, 58 ]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print ("This minute seems a little odd.")
else:
    print("Not an odd minute.")
    
