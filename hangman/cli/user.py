class User:
    @staticmethod
    def ready():
        while True:
            again = input("Ready to play? (y/n) ")
            if again.isalpha() and again.lower() == "y":
                return True
            if again.isalpha() and again.lower() == "n":
                return False
            print("Invalid input.")

    @staticmethod
    def user_input():
        while True:
            user_guess = input("Give me a letter: ")
            if user_guess.isalpha() and len(user_guess) == 1:
                return user_guess.upper()
            print("Invalid input.")

    @staticmethod
    def again():
        while True:
            again = input("Do you want to play again? (y/n) ")
            if again.isalpha() and again.lower() == "y":
                return True
            if again.isalpha() and again.lower() == "n":
                return False
            print("Invalid input.")
