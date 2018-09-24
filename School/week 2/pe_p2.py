letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
letters2 = list(letters)
letters2.sort()
letters3 = [letters2.count('A'), letters2.count('B'),  letters2.count('C')]
print(letters3)
