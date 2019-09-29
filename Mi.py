def Mi():
    print("48+8+2MP AI triple rear camera with portrait mode, HDR, PDAF supported | 32MP front camera with f2.0, 1/2.8 inch pixel size, portrait mode, HDR supported")
    print("15.46 centimeters (6.088-inch) AMOLED multi-touch capacitive touchscreen with 1520 x 720 pixels resolution, 282 ppi pixel density")
    print("Memory, Storage & SIM: 4GB RAM | 64GB internal memory expandable up to 256GB | Dual SIM (nano+nano) dual-standby (4G+4G)")
    print("Android Pie v9.0 operating system with 2.0GHz Qualcomm Snapdragon 665 octa core processor, Adreno 610 GPU")
    print("4030mAH lithium-ion battery, AI Scene detection: Detects up to 27 different scenes")
    print("1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories including batteries from the date of purchase")
    print("Box also includes: Power adapter, USB cable, warranty card, user guide, SIM tray ejection tool and back cover")
    print("The low SAR value(1.6W/kg) of Mi A3 means that a minimal amount of RF energy is absorbed by the body when using a mobile phone, making it extremely safe")
    
    print("                    Price: Rs.12,999                    ")

    final = input("Buy           Add to Cart          Back")
    if final == "Buy" or final == "buy" or final == "1":
        print("Item Purchased")
        print("Returning to Home Screen")
        
    elif final == "Add" or final == "add" or final == "2":
        f = open("Cart", "w")
        lines = ("Mi A3")
        f.writelines(lines)
        print("Item added")
        f.close()
    elif final == "Back" or final == "back" or final == "3":
        print("Returning")
    else:
        print("Incorrect input")
        Mi()
Mi()    
