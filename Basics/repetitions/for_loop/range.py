brightness = int(input("What level of brightness is required?\n"))

for i in range(2, brightness + 1):
    print(f"Beep's brightness level: {'*' * i}\n"
          f"Bop's brightness level: {'*' * i}\n")

print("\nAdjustments complete!")
