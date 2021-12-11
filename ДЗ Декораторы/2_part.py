import sys
import datetime


def timed_output(function):
    original_write = sys.stdout.write

    def wrapper(name):
        sys.stdout.write = my_write
        function(name)
        sys.stdout.write = original_write

    def my_write(string_text):
        if string_text == "\n" or string_text == "":
            original_write(string_text)
        else:
            dttm = datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
            original_write(f"[{dttm}]: {string_text}")

    return wrapper


@timed_output
def print_greeting(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print_greeting("Nikita")

