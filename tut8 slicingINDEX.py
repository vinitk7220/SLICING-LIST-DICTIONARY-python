mystr = "Vinit is a good boy"

print(len(mystr))
print(mystr[5])
print(mystr[:78])
print(mystr[0:78])  # Error nhi dega, jitna hai utna de dega.
# print(mystr[67])  # Error dega, kyoki index[67] exist hi nhi krta, toh us case mai KUCH BHI nhi kr paa raha.
print(mystr[0:5])
print(mystr[:])
print(mystr[0:])
print(mystr[:18])
print(mystr[:19])
print(mystr[0:])
print(mystr[1:])

print(mystr[0:19:2])  # [0]th index lene ke baad, dusre no. ke index (Second index) pr jayega / 2nd no. ke letter pr jayega.
print(mystr[::3])  # [0]th index lene ke baad, 3rd no. ke letter pr jayega, 1st and 2nd letter ko chod dega.
print(mystr[::100])  # Error nhi dega
print(mystr[-5:-2])  # -2 ko include nhi karega, -2 se chota -3 ko le lega.
print(mystr[-19:])
print(mystr[15:17])
print(mystr[15:-2])
print(mystr[::-1])
print(mystr[::-2])

print(type(mystr))
print(mystr.isalnum())
print(mystr.isalpha())  # true if there is no space in b/w my string
print(mystr.endswith("boy"))
print(mystr.count("i"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is", "are"))
# string functions in python (PLS SEARCH ON GOOGLE) and go through that.
