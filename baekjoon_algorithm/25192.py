class GomGom:

    def __init__(self):
        self._count = 0
        self._cache = {}

    def clear_cache(self):
        self._cache = {}

    def receive_message(self):
        message = input()
        if message == "ENTER":
            self.clear_cache()
            return
        if self._cache.get(message):
            return
        self._cache[message] = True
        self._count += 1

    @property
    def count(self):
        return self._count
    
if __name__ == "__main__":
    N = int(input())
    gom = GomGom()
    for _ in range(N):
        gom.receive_message()
    print(gom.count)