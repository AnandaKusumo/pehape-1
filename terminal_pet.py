import time

print("======================================")
print("             DIGITAL PET              ")
print("======================================")

print("\nSelamat datang✨✨✨✨")
time.sleep(1)

def main_menu():
    print("=== Main Menu ===")
    print("1. Start Game")
    print("2. Exit Game")

    choice = input("\nPilih")

    if choice == "1":
        game()

    elif choice == "2":
        print("\nBye-Bye🖐")

def game():
    name = input("\nMasukkan nama peliharaan: ")
    print("\n...")
    time.sleep(1)

    print(f"\n{name} telah datang!")
    print("Jaga dia baik-baik")

    hunger = 50
    happiness = 50
    energy = 50

    while True:
        print("\n==============")
        print(f"{name}")
        print("===============")
        print("Status:")
        print("Hunger   :", hunger)
        print("Happiness:", happiness)
        print("Energy   :", energy)

        print("\n=== Menu ===")
        print("1. Bermain")
        print("2. Tidur")
        print("3. Makan")
        print("4. Exit")

        choice = input("\nPilih > ")

        if choice == "1":
            hunger += 10
            energy -= 15
            happiness += 25
            print(f"\n{name} bersenang-senang!")

        elif choice == "2":
            hunger += 5
            energy += 35
            happiness -= 10
            print(f"\n{name} tidur nyenyak...")

        elif choice == "3":
            hunger -= 25
            energy -= 5
            happiness -= 10
            print(f"\n{name} makan dengan lahap!")

        elif choice == "4":
            print("\nBye🖐")
            break

        else:
            print("\nPilihan tidak valid")

        hunger += 5
        energy -= 2
        happiness -= 5

        hunger = max(0, min(100, hunger))
        energy = max(0, min(100, energy))
        happiness = max(0, min(100, happiness))

        if hunger >= 100:
            print(f"\n{name} mati kelaparan... game over")
            break

        if energy <= 0:
            print(f"\n{name} kelelahan")
            energy = 20

        if happiness <= 0:
            print(f"\n{name} mengalami depresi... game over")
            break

        if hunger <= 0:
            print(f"\n {name} mati obesitas... game over")
            break

        time.sleep(1)

main_menu()