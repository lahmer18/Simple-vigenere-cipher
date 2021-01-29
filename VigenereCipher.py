#This function takes two parameters ,it helps us to fit the key with our plain text even len(key) is less than the len(plaintext)
#Exemple1 : key = "sidahmed",num = 20 ,return = "sidahmedsidahmedsida"
#Exemple2 : key = "blabla",num = "5", return = "blabl"
def cover_plaintext_withKey(key, num):
    rp = num // len(key) + 1
    return (key * rp)[:num]
#We assume that our plaintext is composed just of UpperCaseLetters A..Z
#If plaintext is composed from lowercase and whitespaces , return = eliminate white spaces , convert all letters to upper case
#Zip(arg1,arg2) takes two array arg1,arg2 and return array of tuples => Return = [(arg1[0],arg2[0])....(arg1(len(arg1)-1,arg1(len(arg1)-1))]
class Vigenerecipher:
    def __init__(self,key):
        self.key = key.upper()
    def encrypt(self,plainText):#Enctryption method take our plain text and return a cipher text encrypt(plaintext,self.key)
        cipher = ""
        plainText = plainText.replace(' ','').upper()
        tmpKey = cover_plaintext_withKey(self.key,len(plainText))
        for p,k in zip(plainText,tmpKey):
            ci = ord(p)+ord(k)-130
            ci = ci%26
            ci = chr(ci+65)
            cipher +=ci
        return cipher
    def decrypt(self,cipherText):#Decryption method takes a cipher text and return a originaltext(plaintext) decryption(ciphertext,self.key)
        plainText = ""
        cipherText = cipherText.upper()
        tmpKey = cover_plaintext_withKey(self.key,len(cipherText))
        for c,k in zip(cipherText,tmpKey):
            pt = ord(c)-ord(k)
            pt = pt%26
            pt = chr(65+pt)
            plainText +=pt
        return plainText


