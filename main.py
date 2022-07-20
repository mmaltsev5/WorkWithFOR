d = 'yaichniy belok'
count = 0

for x in d:
    if x == 'b':
        print('Est` bukva "b"')
        count += 1

    if x == 'a':
        print('Skip "a"')
        continue

    if x == 'o':
        print('ZAMECHENA BUKVA "o", TREVOGA')
        print('Cikl zavershen, bukv "B" bilo obnarujeno -',  count)
        break
else:
    print ('Cikl zavershen, bukv "B"',  count)