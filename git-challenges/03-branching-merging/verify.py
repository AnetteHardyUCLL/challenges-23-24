import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'fbe1626fdc1f5bdb48eedc948af4031f3d2585ba', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()