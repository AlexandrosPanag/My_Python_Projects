class ExampleCounterClass:
    x = 2
    def counter(self):
        self.x = self.x * 2
        print(self.x)

callme = ExampleCounterClass()
callme.counter()
callme.counter()