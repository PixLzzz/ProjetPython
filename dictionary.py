import hashing

# Certains utilisent un nom d'animal
def Animals(hashedpwd):
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            hashed = hashing.hashing(animal)
            if hashed in hashedpwd:
                print(animal, hashed)
                return animal,hashed

    f.close()

# Certains ont utilisés la concaténation de 2 animaux
def concatAnimals(hashedpwd):
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            for animal2 in animals:
                hashed = hashing.hashing(animal + animal2)
                if hashed in hashedpwd:
                    print(animal + animal2, hashed)
                    return animal + animal2, hashed


# Certains ont utilisé le nom d'un animal et lui ont rajoutés des chiffres devant ou derrière (max 3) avec ou sans une majuscule a la première lettre de l'animal
def digAnimals(hashedpwd):
    results = ""
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            for x in range(1000):
                tempInt = str(x)
                res = tempInt + animal
                hashed = hashing.hashing(res)
                if hashed in hashedpwd:
                    print(res, hashed)
                    results= results + res + " " + hashed + "\n"
                res = tempInt + animal.capitalize()
                hashed = hashing.hashing(res)
                if hashed in hashedpwd:
                    print(res, hashed)
                    results= results + res + " " + hashed
                res2 = animal + tempInt
                hashed2 = hashing.hashing(res2)
                if hashed2 in hashedpwd:
                    print(res2, hashed)
                    results= results + res + " " + hashed + "\n"
                res2 = animal.capitalize() + tempInt
                hashed2 = hashing.hashing(res2)
                if hashed2 in hashedpwd:
                    print(res2, hashed)
                    results= results + res + " " + hashed
    return results


# Certains prennent le nom d'un animal, le mettent à l'envers, et le dédoublent.
def reverseConcatAnimals(hashedpwd):
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            for animal2 in animals:
                animalRev = animal[::-1]
                animal2Rev = animal2[::-1]
                hashed = hashing.hashing(animalRev + animal2Rev)
                if hashed in hashedpwd:
                    print(animalRev + animal2Rev, hashed)
                    return animalRev + animal2Rev, hashed
    f.close()



# Certains prennent le nom d'un animal, changent toutes les voyelles par un nombre et mettent le tout en majuscule.
def AnimalScramble(hashedpwd):
    listeVoyelles = ["a", "e", "i", "o", "u", "y"]
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            newStr = []
            indexVoy = []
            for i in range(len(animal)):
                if animal[i] in listeVoyelles:
                    indexVoy.append(i)
                newStr.append(animal[i])
            if len(indexVoy) == 1:
                for k in range(10):
                    newStr[indexVoy[0]] = k
                    resStr = "".join(map(str, newStr))
                    animalUp = resStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(resStr, hashed)
                        return resStr, hashed
            if len(indexVoy) == 2:
                for l in range(100):
                    initTab = []
                    formatedl = str(l).zfill(2)
                    initTab.append(formatedl)
                    newStr[indexVoy[0]] = initTab[0][:1]
                    newStr[indexVoy[1]] = initTab[0][1:2]
                    finalStr = "".join(map(str, newStr))
                    animalUp = finalStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(animalUp, hashed)
                        return animalUp, hashed
            if len(indexVoy) == 3:
                for l in range(1000):
                    initTab = []
                    formatedl = str(l).zfill(3)
                    initTab.append(formatedl)
                    newStr[indexVoy[0]] = initTab[0][:1]
                    newStr[indexVoy[1]] = initTab[0][1:2]
                    newStr[indexVoy[2]] = initTab[0][2:3]
                    finalStr = "".join(map(str, newStr))
                    animalUp = finalStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(animalUp, hashed)
                        return animalUp, hashed
            if len(indexVoy) == 4:
                for l in range(10000):
                    initTab = []
                    formatedl = str(l).zfill(4)
                    initTab.append(formatedl)
                    newStr[indexVoy[0]] = initTab[0][:1]
                    newStr[indexVoy[1]] = initTab[0][1:2]
                    newStr[indexVoy[2]] = initTab[0][2:3]
                    newStr[indexVoy[3]] = initTab[0][3:4]
                    finalStr = "".join(map(str, newStr))
                    animalUp = finalStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(animalUp, hashed)
                        return animalUp, hashed
            if len(indexVoy) == 5:
                for l in range(100000):
                    initTab = []
                    formatedl = str(l).zfill(5)
                    initTab.append(formatedl)
                    newStr[indexVoy[0]] = initTab[0][:1]
                    newStr[indexVoy[1]] = initTab[0][1:2]
                    newStr[indexVoy[2]] = initTab[0][2:3]
                    newStr[indexVoy[3]] = initTab[0][3:4]
                    newStr[indexVoy[4]] = initTab[0][4:5]
                    finalStr = "".join(map(str, newStr))
                    animalUp = finalStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(animalUp, hashed)
                        return animalUp, hashed
            if len(indexVoy) == 6:
                for l in range(1000000):
                    initTab = []
                    formatedl = str(l).zfill(6)
                    initTab.append(formatedl)
                    newStr[indexVoy[0]] = initTab[0][:1]
                    newStr[indexVoy[1]] = initTab[0][1:2]
                    newStr[indexVoy[2]] = initTab[0][2:3]
                    newStr[indexVoy[3]] = initTab[0][3:4]
                    newStr[indexVoy[4]] = initTab[0][4:5]
                    newStr[indexVoy[5]] = initTab[0][5:6]
                    finalStr = "".join(map(str, newStr))
                    animalUp = finalStr.upper()
                    hashed = hashing.hashing(animalUp)
                    if hashed in hashedpwd:
                        print(animalUp, hashed)
                        return animalUp, hashed


    f.close()


#Certains concatènent le nom d'un animal et le nom d'un autre animal mis à l'envers
def AnimalAndReverse(hashedpwd):
    with open("Animaux.txt", "r") as f:
        animals = set([line.strip() for line in f])
        for animal in animals:
            finalPwd = []
            finalPwd.append(animal)
            for animal2 in animals:
                finalPwd2 = []
                toStr = "".join(map(str, finalPwd))
                finalPwd2.append(toStr)
                animalRev = animal2[::-1]
                finalPwd2.append(animalRev)
                finalStr = "".join(map(str, finalPwd2))
                hashed = hashing.hashing(finalStr)
                if hashed in hashedpwd:
                    print(finalStr , hashed)
                    return finalStr, hashed
    f.close()