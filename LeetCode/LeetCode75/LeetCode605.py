class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        flowers_left = n
        while i < len(flowerbed) and flowers_left > 0:
            if i == 0:
                if flowerbed == [0]:
                    return n <= 1
                if flowerbed[0:2] == [0, 0]:
                    flowerbed[i] = 1
                    flowers_left -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[len(flowerbed) - 2:] == [0, 0]:
                    flowerbed[i] = 1
                    flowers_left -= 1
            else:
                if flowerbed[i-1:i+2] == [0, 0, 0]:
                    flowerbed[i] = 1
                    flowers_left -= 1
            i += 1
        return flowers_left == 0