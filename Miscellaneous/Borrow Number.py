#https://prepinsta.com/bny-mellon-coding-questions-and-answers/

n1 = int(input())
n2 = int(input())

if n1 < n2:
    print("not possible")
else:
    borrow_count = 0
    borrow = 0

    while n2 > 0:
        d1 = n1 % 10
        d2 = n2 % 10

        if d1 < d2 + borrow:
            borrow = 1
            borrow_count += 1
        else:
            borrow = 0

        n1 //= 10
        n2 //= 10

    print(borrow_count)
