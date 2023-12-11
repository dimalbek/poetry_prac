from file import print_fullname

def test_fullname():
    assert print_fullname('Dimash', 'Albek') == 'my name is Dimash Albek'
    assert print_fullname('yasper', 'moglote') == 'my name is yasper moglote'
