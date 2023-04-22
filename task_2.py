# Have 2 lists, return intersection

def arrayIntersection(a, b):
    intersection = []
    for i in a:
        if i in b:
            intersection.append(i)
            a.remove(i)
            b.remove(i)
    return intersection


a = [0, 1, 2, 1, 1, 3, 4, 5]
b = [1, 3, 7, 5, 1, 9]

print(arrayIntersection(a, b))
