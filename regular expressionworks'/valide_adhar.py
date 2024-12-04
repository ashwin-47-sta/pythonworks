

#3 alphabets
# 4thplace alphabet[PCAFHT]
# 1alphabet
# 4 digit
# 1 alphabet


from re import fullmatch

pancard_number= input("enter pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

mather=fullmatch(pattern,pancard_number)

if mather==None:

    print("invalid")

else:

    print("valid")

