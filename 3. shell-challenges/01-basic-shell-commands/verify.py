import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert (solution == 'a60eb0ab04a573d8744fc384312d4dda141f9afb' or solution == "fd534d4bb3de329346e88e3245ba0d1db69244c0" or solution == "7bf034044650e1b797e32731d2c59a40362740ba" or solution == "45bc523bf08059635886a00afe7b31e2d9f7b9c4"), 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
