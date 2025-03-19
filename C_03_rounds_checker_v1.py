def int_check(to_check):
    while True:
        error = "Please enter an integer that is 1 or more."

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            print(error)
            return "invalid"


to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]


for item in to_test:
    case = item[0]
    expected = item[1]

    actual = int_check(case)

    if actual == expected:
        print(f" ✅✅✅Passed! case: {case}, expected: {expected}, received: {actual}✅✅✅ ")
    else:
        print(f" ❌❌❌Failed! Case: {case}, expected: {expected}, received: {actual}❌❌❌ ")
