# 유클리드 호제법으로 a와 b의 최대공약수 구하기
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)