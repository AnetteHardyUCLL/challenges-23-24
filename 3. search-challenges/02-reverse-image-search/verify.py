import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(
            file.read().strip().lower().encode("utf-8")).hexdigest()

    assert (
        solution == "97f6c9d7e6f83f99f35ba3659c000389d2c9135b"), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
