class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        cel = []
        cel.append(float(celsius + 273.15))
        cel.append(float(celsius * 1.80 + 32.00))
        return cel