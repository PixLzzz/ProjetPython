import hashing

# Certains utilisent leur prénom avec optionnellement des nombres rajoutés (maximum 4) devant ou derrière, avec ou sans une majuscule a la première lettre de leur prénom
def method1(listStudent, hashedpwd):
    for x in range(10000):
        tempInt = str(x)
        for name in listStudent:
            res = tempInt + name
            hashed = hashing.hashing(res)
            if hashed in hashedpwd:
                print(res, hashed)
                return res, hashed
        for prenom in listStudent:
            resbis = prenom + tempInt
            hashedbis = hashing.hashing(resbis)
            if hashedbis in hashedpwd:
                return resbis, hashed


# Certains font la même chose mais on rajouter une lettre (min ou maj) devant leur prénom avant.
def method2(listStudent, hashedpwd):
    for x in range(10000):
        tempInt = str(x)
        for name in listStudent:
            for i in range(26):
                x = chr(i + 65)
                res = tempInt + x + name
                hashed = hashing.hashing(res)
                if hashed in hashedpwd:
                    print(res,hashed)
                    return res, hashed
            for i in range(26):
                xx = chr(i + 97)
                res = tempInt + xx + name
                hashed = hashing.hashing(res)
                if hashed in hashedpwd:
                    print(res,hashed)
                    return res, hashed

        for prenom in listStudent:
            for i in range(26):
                x2 = chr(i + 65)
                res2 = x2 + prenom + tempInt
                hashed2 = hashing.hashing(res2)
                if hashed2 in hashedpwd:
                    print(res2,hashed2)
                    return res2, hashed2
            for i in range(26):
                xx2 = chr(i + 97)
                res2 = tempInt + xx2 + prenom
                hashed2 = hashing.hashing(res2)
                if hashed2 in hashedpwd:
                    print(res2,hashed2)
                    return res2, hashed2


#Certains alternent les minuscules et majuscules dans leur prénom
def UpAndDown(listPrenom ,hashedpwd):
    for nom in listPrenom:
        finalName = []
        done = True
        for char in nom:
            if done==True:
                a = char.upper()
                finalName.append(a)
                done = False
            else:
                finalName.append(char)
                done = True
        finalStr = "".join(map(str, finalName))
        hashed = hashing.hashing(finalStr)
        if hashed in hashedpwd:
            print(finalStr, hashed)
            return finalStr,hashed


        done = False
        for char in nom:
            if done == True:
                a = char.upper()
                finalName.append(a)
                done = False
            else:
                finalName.append(char)
                done = True
        finalStr = "".join(map(str, finalName))
        hashed = hashing.hashing(finalStr)
        if hashed in hashedpwd:
            print(finalStr, hashed)
            return finalStr, hashed