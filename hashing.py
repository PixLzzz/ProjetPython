import hashlib as hash

# HASH en md5
def hashing(strToHash):
    encodedStr = strToHash.encode('utf-8')
    hashStr = hash.md5(encodedStr)

    return hashStr.hexdigest()

