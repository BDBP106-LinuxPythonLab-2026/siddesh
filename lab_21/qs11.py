



from functools import reduce


words = ["Python", "is", "fun", "for", "biologists"]
print("Q11:", reduce(lambda a, b: a + " " + b, words) + ".")