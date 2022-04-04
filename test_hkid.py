from HKID_Verification import verify, calculate
import pytest

def test_valid():
    assert verify("C1234569")
    assert verify("G123456A")
    
def test_invalid():
    assert not verify("AY987654A")
    assert not verify("C1234567")

def test_cal_correct():
    hkid1 = "C123456"
    hkid2 = "S455585"
    assert verify(hkid1 + calculate(hkid1))
    assert verify(hkid2 + calculate(hkid2))

def test_incorrect():
    with pytest.raises(ValueError):
        verify("A123456789")
        verify("asdasd")
        verify("")
    
