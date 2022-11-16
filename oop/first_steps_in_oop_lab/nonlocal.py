def f1():
    count = 0

    def f1_inner():
        def f1_innermost():
            # get from parent scope
            nonlocal count
            count += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count)


def f2():
    count = [0]

    def f1_inner():
        def f1_innermost():
            # get from parent scope
            nonlocal count
            count[0] += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count[0])


f1()
f2()


