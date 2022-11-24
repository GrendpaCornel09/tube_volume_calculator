import math
import os
import time

phi = 22 / 7

print("Input in centimeters.")

while True:
    try:
        r = int(input("What is the radius? "))
    except:
        time.sleep(0.5)
        print("Invalid response. Try again.")
        time.sleep(0.5)
        continue
    break

while True:
    try:
        t = int(input("What is the height? "))
    except:
        time.sleep(0.5)
        print("Invalid response. Try again.")
        time.sleep(0.5)
        continue
    break

volume = round(phi * r * r * t, 2)
surface_area = round((phi * r * r) + (phi * r * r) + (2 * phi * r * t), 2)

print(f"Volume: {volume}")
print(f"Surface area: {surface_area}\n")

def post_program():
    end = input("exit/restart? ")

    if end == "exit":
        exition = "Exiting program..."
        print(exition)
        time.sleep(0.5)
        exition = "Exited."
        print(exition + "\n")
        exit()

    elif end == "restart":
        restart = "Restarting program..."
        print(restart)
        time.sleep(0.5)
        restart = "Program restarted."
        print(restart + "\n")
        os.system("python tube_volume_calculator.py")

    else:
        time.sleep(0.5)
        print("Invalid response. Try again.")
        time.sleep(0.5)
        post_program()

post_program()