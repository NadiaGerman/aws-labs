# Voting System
# This script allows users to vote for candidates and displays the final vote count.

def display_candidates(candidates):
    print("Available candidates:")
    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate}")

def get_vote(candidates):
    try:
        choice = int(input("Enter the number of your chosen candidate: "))
        if 1 <= choice <= len(candidates):
            return candidates[choice - 1]
        else:
            print("Invalid choice. Please choose a number from the list.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    candidates = ["Alice", "Bob", "Charlie"]
    votes = {name: 0 for name in candidates}

    print("Welcome to the Voting System!")
    display_candidates(candidates)

    while True:
        vote = get_vote(candidates)
        if vote:
            votes[vote] += 1
            print(f"Thank you! Your vote for {vote} has been recorded.")

        another = input("Do you want to add another vote? (yes/no): ").lower()
        if another != "yes":
            break

    print("\nFinal Vote Counts:")
    for name, count in votes.items():
        print(f"{name}: {count} votes")

if __name__ == "__main__":
    main()
