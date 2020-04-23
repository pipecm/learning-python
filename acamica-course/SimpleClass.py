class SimpleClass:
    @staticmethod
    def printSomething(text):
        print("Printing {} from static method SimpleClass.printSomething()".format(text))


SimpleClass.printSomething("some content")