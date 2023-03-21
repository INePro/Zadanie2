s = input("Слова - ")

i, j = map(int, input().split())

sub = s[i - 1:j]

res = s[:i - 1] + sub[::-1] + s[j:]

print(res)