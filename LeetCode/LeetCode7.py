class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        new_result = None
        if x < 0:
            new_result = int('-' + x_str[1:][::-1])
        else:
            new_result = int(x_str[::-1])
        if new_result > (2 ** 31 - 1) or new_result < (-1 * 2 ** 31):
            return 0
        else:
            return new_result