votes = {}

def cast_vote():
    candidate = input("Enter candidate name: ")
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    print("Vote cast successfully")

def view_results():
    if not votes:
        print("No votes cast yet")
    else:
        for candidate, count in votes.items():
            print(candidate, "-", count, "votes")

def main():
    while True:
        print("1. Cast Vote")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            cast_vote()
        elif choice == "2":
            view_results()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
