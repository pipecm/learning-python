family = ["Jorge", "Maria", "Patricio", "Felipe", "Matias"]


def print_family():
    for member in family:
        print(member)


def cross_product(a, b):
    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) == 3 and len(b) == 3:
            c = (a[1] * b[2] - a[2] * b[1], a[0] * b[2] - a[2] * b[0], a[0] * b[1] - a[1] * b[0])
            return c
        else:
            raise Exception("Length of both vectors must be equal to 3")
    else:
        raise TypeError("Data type must be tuple")


def isSet(collection):
    return len(collection) == len(set(collection))


def cleanKey(key):
    return " ".join(map(lambda word: word.capitalize(), key.split("_")))


print_family()
siblings = family[2:]
print(siblings)

in_law = ["Claudia", "Anabel"]
family.extend(in_law)
print_family()

a = (4, -6, 3)
b = (-1, 7, 4)
print(cross_product(a, b))
print(cross_product(b, a))

print(family[::-1])     # reverse order

print(isSet(["a", "b", "c"]))
print(isSet(["a", "b", "a"]))

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
setC = {7, 8}
print(setA.intersection(setB))
print(setA.union(setB))

AintC = setA & setC
AuniC = setA | setC
print(AintC if AintC else "empty set")
print(AuniC if AuniC else "empty set")

champions = {"champions_league" : "Liverpool", "europa_league" : "Chelsea", "copa_libertadores" : "Flamengo" }
for tournament, team in champions.items():
    print("The champion of the {} is {}".format(cleanKey(tournament), team))
