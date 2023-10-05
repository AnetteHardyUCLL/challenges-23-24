import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'f2600abb362af63b20620d52319e421e1a43f5c4', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
