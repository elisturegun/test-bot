def greet(name):
    print(f"Hello {name}")  # Example line for the bot to review

def calc(x, y):
    return x + y

def insecure_func(data):
    eval(data)  # 🚨 Intentional security risk to trigger review
