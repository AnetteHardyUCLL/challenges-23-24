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
    
    assert lines[0] == 'a264c67fdbed62ce10be6319b94f26054d54baf1', 'FAIL: line 1 Originating IP is incorrect'
    assert lines[1] == '10b78a2df83719e57a79dc354a05208212ae8ed3', 'FAIL: line 2 Attacker email is incorrect'
    assert lines[0] == 'dbaea2cb42eb8f0e74583c7d4c87b722644ad9ac', 'FAIL: line 3 Victim email is incorrect'

    print("SUCCESS: challenge completed.")
    return True


verify()
