def Amazfit():
    print("UP TO 45 DAYS BATTERY LIFE: A powerful battery capable of lasting up to 45 days on a single charge")
    print("3 ATM WATER RESISTANT: Designed to withstand all your activities rain or shine, this watch is 3 ATM certified, equivalent to about 30 meters water depth")
    print("Mi Fit")
    print("LIGHTWEIGHT: Comfortable to wear day and night; You will even forget it’s there on your wrist")
    print("ACTIVITY and SPORTS TRACKING: Track daily activities and sports like indoor and outdoor running, walking and cycling")
    print("REFLECTIVE ALWAYS-ON: The display is always on and easily readable under bright sunlight")
    print("NOTIFICATIONS: Receive notifications for incoming calls, emails, messages and other apps. Sedentary reminders if you’ve been sitting too long")

    print("                    Price: Rs.3,999                    ")

    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Amazfit Bip Lite")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
Amazfit()    
