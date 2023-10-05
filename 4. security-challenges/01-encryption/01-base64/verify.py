import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '3d665e16b86e482b6885a778ae32113ee244f6d8', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()