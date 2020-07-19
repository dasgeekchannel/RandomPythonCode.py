#Restaurant Bill Calculator
#Created by DasGeek

#Get inputs
total_bill = input("What's the total on the bill? : ")
tip_perc = input("What is the percent of tip you want to leave (Ex: 15, 20) : ")
sharing = input("How many people are sharing the bill? : ")
tip_amount = float(total_bill) * float(tip_perc) / 100 #calculate tip amount converting to floats
print("Tip Amount $", tip_amount) # printing total tip
ftotal = float(total_bill) + float(tip_amount) #creating total of tip and full bill
print("total bill $", ftotal/int(sharing)) #dividing total of bill w/ tip by the amount of people sharing bill


