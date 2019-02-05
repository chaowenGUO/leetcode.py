class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        return z == 0 or x + y >= z and z % math.gcd(x, y) == 0
