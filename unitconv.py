#Unit Converter
#Written by DasGeek
#!/usr/bin/python
#Take US measurements and convert them

# START LOOP
ans=True
while ans:
    print(""" 
    1.Convert inches to centimeters
    2.Convert pounds to kg
    3.Convert fahrenheit to celsius
    4.Exit/Quit
    """) # using triple quotes to print text spanning multiple line
    ans=input("What would you like to do? ") # prompt user for choice from menu above
    if ans=="1":
        inch_conv = input("Enter A Distance In Inches (in to cm): ") #prompt use for distance
        inch_cm = int(inch_conv) * 2.54 #formula to convert in to cm
        print(inch_conv, "inches is equal to", inch_cm, "centimeters") #print text and output
    elif ans=="2":
      kg_conv = input("Enter total pounds: ")
      kg_lbs = float(kg_conv) * 0.45359237
      print(kg_conv, "pounds is equal to", round(kg_lbs,2), "kg") #using round to 2 spaces to reduce decimal spaces
    elif ans=="3":
      fah_conv = input("Enter the temperature in Fahrenheit?: ")
      fah_cel = (int(fah_conv) - 32) / (1.80002)
      print(fah_conv, "Fahrenheit is equal to", round(fah_cel,2), "Celsius")
    elif ans=="4":
      print("\n Goodbye")
      ans = None
    else:
       print("\n Not Valid Choice Try again") #if 1-4 not chosen errors out.


