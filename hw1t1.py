print("Please enter палиндром :")
strForCheck = list(str(input()).upper())
revStr = strForCheck.copy()
revStr.reverse()
if str(strForCheck) == str(revStr):
    print("палиндром")
else:
    print("ни палиндром")