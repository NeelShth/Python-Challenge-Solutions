encrypt_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decrypt_str = ""
for char in encrypt_str:
    if char.isalpha():
        if ord(char) == 121:
            decrypt_str += "a"
        elif ord(char) == 122:
            decrypt_str += "b"
        else:
            decrypt_str += chr(ord(char)+2)
    else:
        decrypt_str += char
#The letters on the paper tell you the ascii character needs to be moved forward by 2
#"i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
#The method I used refers to:"everybody thinks twice before solving this." and "using string.maketrans() is recommended."


trans_str = "".join(chr(num) for num in range(99, 123))
trans_str += "ab"
alphabet = "".join(chr(num) for num in range(97, 123))
trans_table = str.maketrans(alphabet, trans_str)

#This produces the same string
#"i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
#Now use 'trans_table' on "map" as it state in the decrypted string "now apply on the url."

print("map".translate(trans_table))
#Now replace "map.html" with "ocr.html"
