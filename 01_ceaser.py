
alphabet = 'abcdefghijklmnopqrstuvwxyz'

stringText = input("Enter the you want to encrypt")
encryptText = ''
for i in stringText:
    position = alphabet.find(i)
    encryptText+=alphabet[(position+5)%26]
print(encryptText)


stringText = input("Enter the you want to decrypt")
decryptText = ''
for i in stringText:
    position = alphabet.find(i)
    decryptText+=alphabet[(position-5)%26]
print(decryptText)
