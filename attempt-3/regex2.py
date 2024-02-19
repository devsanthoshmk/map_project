import re

text = """gift shop BQZ4ZeL0Jpi4juMP44unqAc 0ahUKEwiii47PqomDAxUYnGMGHePFCXUQmBkIAigA gift shop BQZ4ZeL0Jpi4juMP44unqAc 0ahUKEwiii47PqomDAxUYnGMGHePFCXUQmBkIBCgB BQZ4ZeL0Jpi4juMP44unqAc 0ahUKEwiii47PqomDAxUYnGMGHePFCXUQ8BcIBSgA No2 1538 Chetpet Vandavasi Tamil Nadu 604408 https search google com local reviews placeid u003dChIJXenAnOklUzoR05cm3VfiYj0 u0026q u003dgift shop u0026authuser u003d0 u0026hl u003den u0026gl u003dIN reviews 0ahUKEwiii47PqomDAxUYnGMGHePFCXUQ6W4IFSgA 498139799999999 59830319999999 0x3a5325e99cc0e95d 0x3d62e257dd2697d3 THE GIFT CORNER u0026 CHIP LINE MOBILE SERVICE u0026 ALL TYPE SKINS Gift shop Mobile phone repair shop No2 THE GIFT CORNER u0026 CHIP LINE MOBILE SERVICE u0026 ALL TYPE SKINS 1538 Chetpet Vandavasi Tamil Nadu 604408 Favourites"""

# Extract relevant information using regular expressions
matches = re.findall(r'(gift shop)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)', text)
print(matches)
# Print the results
for match in matches:
    print("Shop Name:", match[0])
    print("Code 1:", match[1])
    print("Code 2:", match[2])
    print("Code 3:", match[3])
    print("----")
