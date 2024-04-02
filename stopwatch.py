# Stopwatch

class Counter:

    def __init__(self, limit):

        self.limit = limit
        self.value = 0


    def set(self, new_value):

        if 0 <= self.value < self.limit:
            self.value = new_value
        else:
            self.value = 0


    def tick(self):

        self.value += 1

        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):

        return str(self.value).zfill(2)


# Test code


counter = Counter(30)


print("Count from 1 to 5")
for i in range(5):
    counter.tick()
print(counter)


print("Reset the counter")
counter.set(0)
print(counter)


print("Set the counter to 27")
counter.set(27)
print(counter)


print("When counter hits 30, it turns to 0")
for i in range(5):
    counter.tick()
    print(counter)
