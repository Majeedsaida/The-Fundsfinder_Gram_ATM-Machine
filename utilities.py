class Utilities:
    @staticmethod
    def get_valid_input(prompt, input_type=int):
        """Prompt the user for input and validate its type."""
        while True:
            try:
                return input_type(input(prompt))
            except ValueError:
                print("Invalid input. Please try again.")
