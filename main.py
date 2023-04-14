#phonenumbers package is used to get info about any phone number.
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your number with '+'country code : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
#To get info in english we are passing 'en' as argument.
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")

#Printing info about provided phone number.
print(phone)
print(time)
print(car)
print(reg)
