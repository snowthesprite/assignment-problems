def finding_probability(tests) :
    for heads in range(4) :
        for test in tests :
        amount_of_heads = 0
        for outcome in test :
            if outcome :
                amount_of_heads += 1
        if amount_of_heads == num_heads :
            succeeded_tests += 1
    return succeeded_tests/test_amount


coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']
