import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        sol_lines = file.readlines()
        assert len(sol_lines) == 12, 'FAIL: solution must be exactly 12 lines long'
        lines = []
        for i in range(12):
            lines.append(sha1(sol_lines[i].strip().lower().encode('utf-8')).hexdigest())

    assert lines[0] == '6e46d598d3853d1bd4aa9b67d666337e76332185', 'FAIL: line 1 should be in the form X0000'
    assert lines[1] == 'beef91347f36641644213aae8a4f26e6015b711a', 'FAIL: line 2 should be in the form X0000'
    assert lines[2] == 'a4eba755ad8f88e2c31f841d6d614e2cdee4cf59', 'FAIL: line 3 should have five words'
    assert lines[3] == 'd22c309e7808e636c8293c6561537b1ad5c78664', 'FAIL: line 4 is a XXX Suite'
    assert lines[4] == '17ba0791499db908433b80f37c5fbc89b870084b', 'FAIL: line 5 is a two digit number'
    assert lines[5] == 'dbdc5b38b21872cfe9ac85a53947942ea2727e82', 'FAIL: line 6 is two words without a space in between'
    assert lines[6] == '047179a9917882e33efb280f452240cdab132b77', 'FAIL: line 7 is a long word made up of several words without spaces in between'
    assert lines[7] == '0f86b3be7e431275f08aa7e32149f3af23df0835', 'FAIL: line 8 is in the form xxx-xxxxx'
    assert lines[8] == '5a5179f1dd43b9144a917e744c408409444d73dd', 'FAIL: line 9 is one word starting with k'
    assert lines[9] == '90da6d587952f030daa7f854db374396ad81ad8a', 'FAIL: line 10 should be in the form X0000.000'
    assert lines[10] == '210bb2ae96af2277f0d511df4bbe28bd38a5e8be', 'FAIL: line 11 should be in the form 00.00.000.000'
    assert lines[11] == '2b46e7f3ebce8a77c5e49a32c9526ec97d76694d', 'FAIL: line 12 should be in the form X0000.000'


    print("SUCCESS: challenge completed.")
    return True


verify()
