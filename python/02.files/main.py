username = input("Enter your name: ")

with open("names.txt", "a") as file:
    file.write(username + "\n")

answer = input("Do you want to show all users [y/n]: ")

if answer.lower() == "y":
    with open("names.txt", "r") as file:
        for n in file:
            print(n.strip())
