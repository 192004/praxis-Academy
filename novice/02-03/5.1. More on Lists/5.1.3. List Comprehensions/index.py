# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
([weapon.strip() for weapon in freshfruit])
[(x, x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])