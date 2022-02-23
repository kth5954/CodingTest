import time

def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


dt = [0] * 100
def fibo_top_down(x):
    print('f(%s)' % str(x), end=" ")  # 실행되는 함수 체크
    if x == 1 or x == 2:
        return 1
    if dt[x] != 0:
        return dt[x]
    dt[x] = fibo_top_down(x - 1) + fibo_top_down(x - 2)
    return dt[x]


db = [0] * 100
def fibo_bottom_up(x):
    db[1], db[2] = 1, 1
    for i in range(3, x + 1):
        print('f(%s)' % str(i), end=" ")  # 실행되는 함수 체크
        db[i] = db[i - 1] + db[i - 2]
    return db[x]


start_time = time.time()
fibonacci(10)
print("basic: ", (time.time() - start_time)*100)

start_time = time.time()
fibo_top_down(10)
print("Top-Down: ", (time.time() - start_time)*100)

start_time = time.time()
fibo_bottom_up(10)
print("Bottom-Up: ", (time.time() - start_time)*100)