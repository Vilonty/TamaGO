class main:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):

        return 'main({}, {})'.format(self.x, self.y)

    def __str__(self):

        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):

        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self,other):

        return (self.x > other.x) and (self.y > other.y)

    def __add__(self, other):

        return main(self.x + other.x, self.y + other.y)

x = main(1,2)
y = main(2,3)
print(x)
print(y)

print(x + y)

print(x == y)

print(x > y)
print(x < y)