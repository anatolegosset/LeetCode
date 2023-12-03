class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        potential_angle = abs(30 * (hour % 12) + minutes / 2 - 6 * minutes)
        return min(potential_angle, 360 - potential_angle)