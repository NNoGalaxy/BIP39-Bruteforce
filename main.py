import os, sys, hashlib, urllib.request

entropy = os.urandom(16)    

binary = ""
for byte in entropy:
    binary += str(bin(byte))[2:].rjust(8, "0")


sha256_hash = hashlib.sha256()
sha256_hash.update(entropy)

checksum = str(bin(sha256_hash.digest()[0]))[2:].rjust(8, "0")[:4]
print("checksum = " + checksum)


binary += checksum
print("Entropy + checksum: {}".format(binary))


#https://stackoverflow.com/a/48707091
size = 11
chunks = [binary[y-size:y] for y in range(size, len(binary)+size,size)]



print("Word index: ", end="")
words = []
for chunk in chunks:
    words.append(int(chunk, 2))
    print(int(chunk, 2), end=" ")
print("\n")



with open("wordlist.txt", "r") as wordlist:
    wordlist = wordlist.readlines()
    print("Seed phrase: ")
    for word in words:
        print(wordlist[word][:-1], end=" ")

