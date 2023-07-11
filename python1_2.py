
print(" *** Wind classification ***")
wind_speed = float(input("Enter wind speed (km/h) : "))

if wind_speed < 52.00 :
    level = "Breeze."
elif wind_speed < 56.00 :
    level = "Depression."
elif wind_speed < 102.00:
    level = "Tropical Storm."
elif wind_speed < 209.00 :
    level = "Typhoon."
elif wind_speed >= 209.00 :
    level = "Super Typhoon."
else :
    level = "..."

print(f"Wind classification is {level}")



