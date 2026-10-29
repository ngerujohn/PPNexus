class French:
    def say_hello(self):
        print("Bonjour")

class Kiswahili:
    def say_hello(self):
        print("Habari")

def intro(lang):
    lang.say_hello()

John = French()
Mike = Kiswahili()

intro(John)
intro(Mike)