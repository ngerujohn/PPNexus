
temperature = float(input("Enter current room temperature:"))

if temperature > 25:
    print("Too hot!!")

elif temperature < 25:
    print("Too cold!!")

elif temperature == 25:
    print("Normal temperature!")

else:
    print("Invalid temperature!")
