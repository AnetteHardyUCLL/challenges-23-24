import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        sol_lines = file.readlines()
        assert len(sol_lines) == 7, 'FAIL: solution must be exactly 7 lines long'
        lines = []
        for i in range(7):
            lines.append(sha1(sol_lines[i].strip().lower().encode('utf-8')).hexdigest())

    assert lines[0] == 'e6f02649e2025c594b7aa916e6a60af79ce269b0', 'FAIL: line 1 should be 3 letters corresponding to Active versus Passive Reconnaissance'
    assert lines[1] == '5b7e8e2c878293a489f06f0e542f499d767a781c', 'FAIL: line 2 should be 7 digits corresponding to Google Dorking'
    assert lines[2] == 'fe96f60add12a64b8e275edd03a1fd1762264b5e', 'FAIL: line 3 should be the name of the registrar of UCLL website'
    assert lines[3] == 'b6e184f19d9c481428b404a7558df705b40f21c7', 'FAIL: line 4 should be an abbreviation of an information protection law'
    assert lines[4] == '64c9a9df83db46189717856e0db1a3489cd20495', 'FAIL: line 5 should be the name of the registrar of Microsoft website'
    assert lines[5] == '85f1002bf139bebdb7f0d07b31fa14155aea9dfc', 'FAIL: line 6 should be a 3 digit IANA ID number'
    assert lines[6] == '2ee6c5ac27eaa92922a5b6db3ef35665dfb13997', 'FAIL: line 7 should be the Tech Email address; form: abc@jkl.com'

    print("SUCCESS: challenge completed.")
    return True


verify()
