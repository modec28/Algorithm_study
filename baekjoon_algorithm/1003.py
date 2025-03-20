class Mem:
    cache_value: dict = {0: {0: 1, 1:0}, 1:{0: 0, 1: 1}}

    @classmethod
    def get_cache(cls, key: int):
        return cls.cache_value.get(key)
    
    @classmethod
    def set_cache(cls, key: int, value: str) -> None:
        cls.cache_value[key] = value

def fibonacci(n: int):
    cached_value = Mem.cache_value.get(n)
    if n < 2:
        return cached_value
    if not cached_value:
        prev_1step = fibonacci(n-1)
        prev_2step = fibonacci(n-2)
        value = {
            0: prev_1step[0] + prev_2step[0],
            1: prev_1step[1] + prev_2step[1],
        }
        Mem.set_cache(n, value)
        return value
    else:
        return cached_value

if __name__ == "__main__":
    answer_list = []
    for _ in range(int(input())):
        input_num = int(input())
        data = fibonacci(input_num)
        answer_list.append(f"{data[0]} {data[1]}")
    for answer in answer_list:
       print(answer)
