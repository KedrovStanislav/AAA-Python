import sys


def redirect_output(filepath):
    def decorator(function):
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            sys.stdout = open(filepath, "w")
            function(*args, **kwargs)
            sys.stdout.close()
            sys.stdout = original_stdout

        return wrapper

    return decorator


@redirect_output("./function_output.txt")
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=" ")
        print()


if __name__ == "__main__":
    calculate()
    with open("./function_output.txt", "r") as file:
        print(file.read())

