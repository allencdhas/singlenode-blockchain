import hashlib

datas = []

string = input("Enter data: ")
nonce = 0
hash = ''

def findhash(string):
    global nonce
    global hash
    hash = hashlib.sha256(string.encode()).hexdigest()
    while hash[0:4] != '0000':
        nonce += 1
        hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()

def addblock(datas):
    block = len(datas) + 1
    global nonce
    data = string
    global hash
    datas.append({'block':block, 'nonce':nonce, 'data':string, 'hash': hash})
    #block':block, 'nonce':nonce, 'data':string, 'hash': hash


findhash(string)
addblock(datas)
print("Blockchain: ", datas, end='')