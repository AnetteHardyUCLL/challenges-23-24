import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(
            file.read().strip().lower().encode("utf-8")).hexdigest()

    assert (
        solution == "4bf1beda2cc2aa8ce527de50f0c37c0319ced9bf" or solution == "0776afaaaefe43667efad786941b12b4cd458a31"), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
