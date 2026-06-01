#closure example
def closure():
    x="Hello Closure"
    def inner():
        print(x)
    return inner
f=closure()
f()

#multiple closure example
def multiplier(x):
    def inner(y):
        return x*y
    return inner
double = multiplier(2)
triple = multiplier(3)
print(double(5)) #10
print(triple(5)) #15

def track_tokens():
    total_tokens=0
    def add_tokens(token):
        nonlocal total_tokens
        total_tokens+=token
        print(total_tokens)
    return add_tokens
token_tracker = track_tokens()

token_tracker(50)
token_tracker(100)
token_tracker(200)