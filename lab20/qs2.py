
# qs 2

a = str(input("Enter your sentence: "))
s = list(" ".join(a))

n = len(s)
vowels = ['a', 'e', 'i', 'o', 'u']
print(s)


cV = 0
cC = 0
cD = 0
cS = 0
for i in range(n):
    #print("out side the if cases ",s[i])
    if s[i].isalpha():
        print(s[i])
        if s[i] == vowels[cV]:
            cV += 1
        else :
            cC += 1
    elif s[i].isdigit():
        cD += 1

    elif s[i] == " ":
        cS += 1


print("vowel count: ",cV)
print("consonants count: ",cC)
print("digits count: ",cD)
print("space count: ",cS)
