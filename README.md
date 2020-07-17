# Hong-Kong-ID-Card-verification-algorithm
[![Python package](https://github.com/KnugiHK/Hong-Kong-ID-Card-Verification-Algorithm-MultiLang/workflows/Python%20package/badge.svg)](https://github.com/KnugiHK/Hong-Kong-ID-Card-Verification-Algorithm-MultiLang/actions)

An algorithm for verifying Hong Kong ID Card number.

# Features
1. Verify a HKID
1. Calculate check digit for a HKID

# Supported Language
1. Python (Development)
1. JavaScript  (May not up-to-date and higher translation priority)
1. C# (May not up-to-date and lower translation priority)

# Usage
## Python
*This algorithm is now support Python 2 and 3*
**Run in shell**
```shell
python HKID_Verification.py
Please provide your Hong Kong ID Card number including letter and digit in bracket such as "L5555550" (For security reason, value you typed will not be displayed): AY987654A
```
**Run as library**
```python
from HKID_Verification import verify 
ID = "AY987654A"
print(verify(id))
```

## JavaScript
Place .js file in the path you want and add a <script> tag to link the file to webpage and call function with "HKIDverification(id)" where "(id)" is target HKID Card number
## C#
To-Do....

# To-Do
1. New feature: HKID Card number generator
2. Documentation and usage
