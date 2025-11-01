class Computer:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 0 <= value <= 100:
            self._temperature = value
            if value > 80:
                print("🔥 Ogohlantirish: harorat juda yuqori!")
        else:
            print("⚠️ Harorat 0°C dan 100°C gacha bo‘lishi kerak!")



