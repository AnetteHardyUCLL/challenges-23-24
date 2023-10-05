import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '0aad6cbbd31e5018a84c00721b0877164c732c4d', 'FAIL: the solution should be 1 line with 1 word on it, starting with p'

    print("SUCCESS: challenge completed.")
    return True


verify()
