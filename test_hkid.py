from HKID_Verification import verify, calculate

def test_valid():
    assert verify("C1234569") == True
    assert verify("G123456A") == True
    
def test_invalid():
    assert verify("AY987654A") == False
    assert verify("C1234567") == False

def test_cal_correct():
    hkid1 = "C123456"
    hkid2 = "S455585"
    assert verify(hkid1 + calculate(hkid1)) == True
    assert verify(hkid2 + calculate(hkid2)) == True

def test_incorrect():
    try:
        verify("A123456789")
        verify("asdasd")
        verify("")
    except ValueError:
        _pass = False
    assert _pass == False
    