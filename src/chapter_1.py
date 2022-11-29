from pcinput import getFloat
from pcinput import getInteger
from pcinput import getLetter
from pcinput import getString


def main():
    integer_value = getInteger("enter integer: ")
    print(f"got integer: {integer_value!r}")

    string_value = getString("enter string: ")
    print(f"got string: {string_value!r}")

    float_value = getFloat("enter float: ")
    print(f"got float: {float_value!r}")

    letter_value = getLetter("enter letter: ")
    print(f"got letter: {letter_value!r}")


if __name__ == '__main__':
    main()
