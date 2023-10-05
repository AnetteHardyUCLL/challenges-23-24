import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        sol_lines = file.readlines()
        assert len(sol_lines) == 5, 'FAIL: solution must be exactly 5 lines long'
        lines = []
        for i in range(5):
            lines.append(sha1(sol_lines[i].strip().lower().encode('utf-8')).hexdigest())
   
    assert lines[0] == '0c03a716279d84575bb1d832a28b6f2e628ea10a', 'FAIL: line 1 is a long MD5 hash'
    assert lines[1] == 'ee5974ec6043730f5271eca34369a289be971a76', 'FAIL: line 2 is an identifier, starting with T'
    assert lines[2] == '7cdf5afb2b932d5ecf83fa60efe7766b72917b77', 'FAIL: line 3 consists of 2 words: D____ E____'
    assert lines[3] == 'c9fdf2f1739c8b3e760ee0c6653957c42d4a541c', 'FAIL: line 4 is one word only, O_____on'
    assert lines[4] == '6037b7012db340e4304275f6ca0a7c5a0952fcbd', 'FAIL: line 5 should be in the form: flag{___________}'

    print("SUCCESS: challenge completed.")
    return True


verify()
