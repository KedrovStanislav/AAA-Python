import sys
import datetime


def my_write(string_text):
    if string_text == "\n" or string_text == "":
        original_write(string_text)
    else:
        dttm = datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        original_write(f"[{dttm}]: {string_text}")


if __name__ == "__main__":
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write

