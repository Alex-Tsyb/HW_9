def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"Error: {str(e)}"

    return wrapper


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def handle_hello(self):
        return "How can I help you?"

    @input_error
    def handle_add(self, params):
        name, phone = params.split()
        self.contacts[name] = phone
        return f"Contact {name} added with phone number {phone}"

    @input_error
    def handle_change(self, params):
        name, phone = params.split()
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed to {phone}"
        else:
            raise KeyError(f"Contact {name} not found")

    @input_error
    def handle_phone(self, name):
        if name in self.contacts:
            return f"The phone number for {name} is {self.contacts[name]}"
        else:
            raise KeyError(f"Contact {name} not found")

    @input_error
    def handle_show_all(self):
        if self.contacts:
            return "\n".join(
                f"{name}: {phone}" for name, phone in self.contacts.items()
            )
        else:
            return "No contacts available."

    def main(self):
        while True:
            command = input("Enter command: ").lower()

            if command in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print(self.handle_hello())
            elif command.startswith("add"):
                print(self.handle_add(command[4:]))
            elif command.startswith("change"):
                print(self.handle_change(command[7:]))
            elif command.startswith("phone"):
                print(self.handle_phone(command[6:]))
            elif command == "show all":
                print(self.handle_show_all())
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    bot = AssistantBot()
    bot.main()
