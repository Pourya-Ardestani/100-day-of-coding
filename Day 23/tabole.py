n_str = input().split()
n = int(n_str[0])
m = int(n_str[1])
gosht_1 = 0
gosht_2 = 0



for _ in range(0, n):
    somestring = input()
    gosht_1 += somestring.count('*')
for _ in range(0, n):
    somestring = input()
    gosht_2 += somestring.count('*')
print(gosht_1, end=' ')
print(gosht_2)