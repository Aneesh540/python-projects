import sys

"""
This is just a basic example of command line arguments in python,
if you want you can use it in your own code and to execute this script
you must use "python args_multiply.py (arg1) (arg2)".
"""


def get_args():
    args = sys.argv

    # We don't need the first argument (name of the script)

    args = args[1:]

    # Checkes if there are only two arguments and they are digits

    if len(args) == 2:
        if args[0].isdigit() and args[1].isdigit():

            # Return both as integers so we can multiply

            return int(args[0]), int(args[1])

        # If the arguments are not numbers raise an exception

        else:
            raise Exception("The arguments must be numbers")

    # If there are more than two arguments raise an exception

    else:
        raise Exception("The number required for this program to work is 2, you put " + str(len(args)) + " arguments")

if __name__ == "__main__":
    x, y = get_args()
    print(x * y)
