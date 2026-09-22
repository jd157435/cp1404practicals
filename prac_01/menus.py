name = input("Name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Message")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
print("Finished.")
