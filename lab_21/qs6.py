


o = int(input("enter the number of oxygen : "))
g = int(input("enter the number of glucose : "))
x = o / 6

if g == x:
    print("number of atp are: ", 38*g)

elif g > x:
    print("number of atp are: ", 38*x)

else : # g < x:
    print("number of atp are: ", 38*g)

# print(38*g if g==x else 38*g )
print(38 * g if g == x else (38 * x if g > x else 38 * g))







def cell_metabolism(glucose, oxygen):
    def energy_output():
        # 1 glucose + 6 O2 -> 38 ATP; oxygen can limit the reaction
        reactions = min(glucose, oxygen // 6)
        return reactions * 38
    return energy_output()

print(" ATP produced:", cell_metabolism(10, 42))  # 7 reactions -> 266