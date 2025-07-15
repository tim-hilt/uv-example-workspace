import argparse

from core import hello  # , fibonacci
from native.native import nth_fibonacci_recursive as fibonacci


def parse_args():
    parser = argparse.ArgumentParser(description="Example CLI application")
    parser.add_argument("--greet", action="store_true", help="Print a greeting message")
    # Add argument to calculate Fibonacci number
    parser.add_argument(
        "--fibonacci",
        type=int,
        help="Calculate the Fibonacci number at the given position",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print(
        "uv workspace cli for demonstration purposes. Use --greet or --fibonacci options."
    )

    if args.greet:
        print(hello())

    if args.fibonacci is not None:
        print(fibonacci(args.fibonacci))
