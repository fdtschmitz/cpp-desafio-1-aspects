import aspectlib

# Aspect: Logging
@aspectlib.Aspect
def log_aspect(*args, **kwargs):
    print(f"Logging: Called function {args[0].__name__} with args: {args[1:]}, kwargs: {kwargs}")

# Aspect: Exception Handling
@aspectlib.Aspect
def exception_aspect(*args, **kwargs):
    try:
        yield
    except Exception as e:
        print(f"Exception: {e}")

# Aspect: Timing
@aspectlib.Aspect
def timing_aspect(*args, **kwargs):
    import time
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Timing: Function {args[0].__name__} executed in {end_time - start_time} seconds")

# Apply aspects to functions
@log_aspect
def greet(name):
    print(f"Hello, {name}!")

@exception_aspect
def divide(a, b):
    result = a / b
    print(f"The result is {result}")

@timing_aspect
def fibonacci(n):
    if n <= 0:
        raise ValueError("Invalid input!")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Invoke functions
greet("Alice")
divide(10, 2)
divide(10, 0)
print(fibonacci(5))
