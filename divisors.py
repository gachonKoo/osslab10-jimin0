import sys

number = int(sys.argv[1])

# 약수 찾기
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()
