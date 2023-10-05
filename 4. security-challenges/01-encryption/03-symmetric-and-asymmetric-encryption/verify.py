import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'cb3a4183d935bd6f641023485a4db532df7eee91', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
