def count_capital_small(s):
    small_counter = 0
    capital_counter = 0
    for c in s:
        if c.isalpha():
            if c.islower() == c:
                small_counter+=1
            else:
                capital_counter+=1
        return capital_counter, small_counter

st = input("phrase")
print(count_capital_small())