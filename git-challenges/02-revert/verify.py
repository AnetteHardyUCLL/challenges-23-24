import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '8ab3362e8614372dabe395fa77d444a19e380963', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
