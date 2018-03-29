
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:42:26 2018

@author: Binish125
"""
import random

random.seed(3)

class mono:
    key=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def __init__(self):
        random.shuffle(self.key)
        
    def encrypt(self,plain_text):
        cipher_list=[]
        plain_list=list(plain_text)
        for chara in plain_list:
            if(ord(chara)!=32):
                char_code=ord(chara)%97
                cipher_char=self.key[char_code]
            else:
                cipher_char=" "
            cipher_list.append(cipher_char)
        cipher_text="".join(cipher_list)
        return(cipher_text)
      
    def decrypt(self,cipher_text):
        cipher_list=[]
        plain_list=[]
        cipher_list=list(cipher_text)
        for chara in cipher_list:
            if(ord(chara)!=32):
                char_index=self.key.index(chara)
                char_code=char_index+97
                plain_char=chr(char_code)
            else:
                plain_char=" "
            plain_list.append(plain_char)
        plain_text="".join(plain_list)
        return(plain_text)
        
        
x=mono()
plain_text=input("\nEnter text")
cipher_text=x.encrypt(plain_text)
print("\n\nEncrpted text:\t"+cipher_text)
plain_text=x.decrypt(cipher_text)
print("\n\nDecrypted text:\t"+plain_text)

