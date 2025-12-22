class Rainbow:

    def __init__(self):
        self._rainbow = {
            "ChongChong": True
        }
    
    def dance(self, a: str, b: str):
        if self._rainbow.get(a) or self._rainbow.get(b):
            self._rainbow[a] = True
            self._rainbow[b] = True
    
    @property
    def count_dancer(self):
        return len(self._rainbow)

N = int(input())
gom = Rainbow()
for _ in range(N):
    person1, person2 = input().split()
    gom.dance(person1, person2)
print(gom.count_dancer)
