import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        sol_lines = file.readlines()
        assert len(sol_lines) == 3, 'FAIL: solution must be exactly 3 lines long'
        lines = []
        for i in range(3):
            lines.append(sha1(sol_lines[i].strip().lower().encode('utf-8')).hexdigest())

    assert lines[0] == 'f9d73b9fc903b1ad52fc208a01b32f14f3028582', 'FAIL: line 1 should be of the form: xxx{xxxx_xxxxx_xxxx} '
    assert lines[1] == '44e634c0c6ff0b95ffdfba51e87d81c894245df3', 'FAIL: line 2 should be one word beginning with A'
    assert lines[2] == '1a6cdd3879a00aea49cc8d3bd03ac3e9133e5a10', 'FAIL: line 3 should be exactly three letters'

    print("SUCCESS: challenge completed.")
    return True


verify()
