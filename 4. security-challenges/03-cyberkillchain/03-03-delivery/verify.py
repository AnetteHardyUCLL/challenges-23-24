import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'ebe810838ef56236c7e1fadf0cb632748055d95a', 'FAIL: the solution is one line in the form: ___{__________}'

    print("SUCCESS: challenge completed.")
    return True


verify()
