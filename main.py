
# if condition using this
greeting = "good morning"
if greeting == "good morning":
    print("condition matches")
else:
    print("condition do not match")
# for loop
obj = [1, 2, 3, 4, 5]
for i in obj:
    print(i*2)


# sum of first natural numbers 1+2+3+4+5=15
summation = 0
for j in range(1, 6):
    summation = summation+j
    print(summation)
# while condition
it = 4
while it > 1:
    print(it)
    it = it-1
print("condition  is true")
# break condition using
it = 4
while it > 1:
    if it == 3:
        break
    print(it)
    it = it-1

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
