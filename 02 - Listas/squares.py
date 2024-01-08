squares = []

for valor in range(1, 11):
    squares.append(valor**2)
    
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehensions
squares1 = [valor**2 for valor in range(1,11)]
print(squares1)
