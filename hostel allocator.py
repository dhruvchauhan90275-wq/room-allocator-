print("===================================")
print("       HOSTEL ROOM ALLOCATOR")
print("===================================")

# Available rooms/beds
three_bed = int(input("Enter number of 3-bedded rooms: "))
four_bed = int(input("Enter number of 4-bedded rooms: "))
bunk_bed = int(input("Enter number of bunk bed rooms: "))
two_bed = int(input("Enter number of 2-bedded rooms: "))
flat_bed = int(input("Enter number of 4-bedded flat bed rooms: "))

print("\nRoom availability updated successfully!")

# Number of students
n = int(input("\nEnter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")

    print("\nRoom Types:")
    print("1. 3-bedded room")
    print("2. 4-bedded room")
    print("3. Bunk bed room")
    print("4. 2-bedded room")
    print("5. 4-bedded flat bed room")

    choice = int(input("Enter your preferred room type (1-5): "))

    if choice == 1:
        if three_bed > 0:
            print(name, "has been allocated a 3-bedded room.")
            three_bed -= 1
        else:
            print("Sorry, 3-bedded rooms are not available.")

    elif choice == 2:
        if four_bed > 0:
            print(name, "has been allocated a 4-bedded room.")
            four_bed -= 1
        else:
            print("Sorry, 4-bedded rooms are not available.")

    elif choice == 3:
        if bunk_bed > 0:
            print(name, "has been allocated a bunk bed room.")
            bunk_bed -= 1
        else:
            print("Sorry, bunk bed rooms are not available.")

    elif choice == 4:
        if two_bed > 0:
            print(name, "has been allocated a 2-bedded room.")
            two_bed -= 1
        else:
            print("Sorry, 2-bedded rooms are not available.")

    elif choice == 5:
        if flat_bed > 0:
            print(name, "has been allocated a 4-bedded flat bed room.")
            flat_bed -= 1
        else:
            print("Sorry, 4-bedded flat bed rooms are not available.")

    else:
        print("Invalid choice!")

# Final availability
print("\n===================================")
print("       FINAL ROOM AVAILABILITY")
print("===================================")

print("3-bedded rooms:", three_bed)
print("4-bedded rooms:", four_bed)
print("Bunk bed rooms:", bunk_bed)
print("2-bedded rooms:", two_bed)
print("4-bedded flat bed rooms:", flat_bed)

print("\nThank you for using Hostel Room Allocator!")