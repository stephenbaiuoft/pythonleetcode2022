"""Console script for py_leetcode."""

import fire


def help():
    print("py_leetcode")
    print("=" * len("py_leetcode"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
