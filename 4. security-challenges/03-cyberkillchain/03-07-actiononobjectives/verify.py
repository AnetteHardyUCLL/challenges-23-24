import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'f65bdd6ec85a96a86bb68094998b317d2119267c', 'FAIL: the solution should be one line with one word only'

    print("SUCCESS: challenge completed.")
    return True


verify()
