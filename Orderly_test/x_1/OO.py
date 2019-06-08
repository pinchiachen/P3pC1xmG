class Phone():
    def __init__ (self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

class google_phone(Phone):
    def __init__(self):
        super().__init__(price = 10, camera_count = 3, screen_size = 5)

    def special_freature(self, nums: [int]) -> int:
        res = 1
        for i in nums:
            res *= i
        return(res)

class taiwan_phone(Phone):
    def __init__ (self):
        super().__init__(price = 20, camera_count = 1, screen_size = 3)

    def special_freature(self, nums: int) -> int:
        if nums == 0:
            return(nums)
        elif nums == 1:
            return(nums)
        else:
            a = 0
            b = 1
            for i in range(1, nums):
                c = a + b
                a = b
                b = c
            return(c)

class apple_phone(Phone):
    def __init__ (self):
        super().__init__(price = 30, camera_count = 2, screen_size = 10)

    def special_freature(self, x: int, y: int) -> int:
        res = 1
        for i in range(y):
            res *= x
            x -= 1
        return(res)


