from HKID_Verification import verify, calculate, guess_once
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

def test_guess_once():
    assert guess_once("C123456*") == ["C1234569"]
    assert guess_once("C1234*69") == ["C1234569"]
    assert guess_once("C12*4569") == ["C1234569"]
    assert guess_once("AY987654*") == ["AY9876549"]
    assert guess_once("AY987*549") == ['AY9871549', 'AY9876549']
    assert guess_once("**9876549") == ['WX9876549']
    assert guess_once("*1234569") == [
        "C1234569",
        "N1234569",
        "Y1234569"
    ]
    with pytest.raises(ValueError):
        guess_once("**234569")
        guess_once("C123**69")
