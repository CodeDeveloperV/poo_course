def decorator(func):
    def func_wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")
    return func_wrapper()


@decorator
def say_hello():
    print("Hello")


decorator(say_hello)
