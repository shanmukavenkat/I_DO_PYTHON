#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Your friend John has been given a sentence S and asked to modify it
#by replacing each letter with its previous letter in the alphabet as
#shown in the table A becomes Z, B becomes A, etc.)
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#input:- Fourty Nine
#output:- Entqsx Mhmd
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


word = input()

s = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
l = list("bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA ")
k = dict(zip(l,s))
res = ""
for i in word:
    res += k[i]
print(res)