name1 = input("Please enter name 1::")
name2 = input("Please enter name 2::")

t = r = u = e = 0
l = o = v = 0
for i in name1.upper() + name2.upper():
    if i == 'T':
        t += 1
    elif i == 'R':
        r += 1
    elif i == 'U':
        u += 1
    elif i == 'E':
        e += 1
    else:
        pass

for i in name1.upper() + name2.upper():
    if i == 'L':
        l += 1
    elif i == 'O':
        o += 1
    elif i == 'V':
        v += 1
    else:
        pass
love_score = int(str(t+r+u+e) + str(l+o+v+e))
print(f"The Love Calculator is calculating your score...\n Your score is {love_score}")

if love_score < 10 or love_score > 90:
    print("message 1")
elif love_score > 40 and love_score < 55:
    print("message 2")
else:
    print("message 3")

