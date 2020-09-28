def finding_probability(tests) :
    all_tests = []
    for num_heads in range(4) :
        succeeded_tests = 0
        for test in tests :
            amount_of_heads = 0
            for outcome in test :
                if outcome == 'H' :
                    amount_of_heads += 1
            if amount_of_heads == num_heads :
                succeeded_tests += 1
        all_tests.append(succeeded_tests/25)
    return all_tests
