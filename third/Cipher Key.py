##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#A Keyword Cipher is a monoalphabetic substitution cipher which uses
#a key to provide encryption on given string of message.
#In a substitution cipher each letter of the plaintext alphabet is
##matched with a different letter according to the ciphertext alphabet.
#Using these letter matchings, every letter of the message is
#substituted to get the encrypted message

#input For example, if the key is zebras ,
#Plaintext Alphabet : a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
#Ciphertext Alphabet : z|e|b|r|a|s|c|d|f|g|h|i|j|k|l|m|n|o|p|q|t|u|v|w|x|y
#Notice that with this key, we are able to match each letter of english
#alphabet with a different letter. Using these matchings we can
#encrypt the word discovered as rfpbluaoar . ( d is replaced with
#r , i is replaced with f , and so on ...)
#Given a key K and the message M , encrypt the message with
#Keyword Cipher, using the given key.
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

k,m = input().split()
s = "abcdefghijklmnopqrstuvwxyz"
letter = list(s)
key = ""
for i in k:
    if i not in key:
        key += i
for i in s:
    if i not in key:
        key += i

key = list(key)
dict1 = dict(zip(letter,key))
res = ""
for i in m:
    res += dict1[i]
print(res)