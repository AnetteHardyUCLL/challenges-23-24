import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        sol_lines = file.readlines()
        assert len(sol_lines) == 4, 'FAIL: solution must be exactly 4 lines long, one statement from Prerequisites and 3 questions under Challenge'
        lines = []
        for i in range(4):
            lines.append(sha1(sol_lines[i].strip().lower().encode('utf-8')).hexdigest())

    assert lines[0] == '17d555cdaf4cb27e721e5918e174ada78a83c39f', 'FAIL: recheck line 11 of the assignment'
    assert lines[1] == '86dfec61b81ea611a060fa005b6fe81189cd430e', 'FAIL: your answer to question 1 is incorrect'
    assert lines[2] == '0a92fab3230134cca6eadd9898325b9b2ae67998', 'FAIL: question 2 is incorrect, use a search engine to find the answer, hint: unidentified'
    assert lines[3] == '4d7ec73ba10524e9afd7cbd52386f2b70e1f6556', 'FAIL: question 3 is incorrect, reread the Cyber threat actors Movtivations section'

    print("SUCCESS: challenge completed.")
    return True


verify()
