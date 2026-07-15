import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Please enter a length of at least 4.")
                continue

            password = generate_password(length)
            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (y/n): ").lower()
            if again != "y":
                print("Goodbye!")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()