# include <iostream>
# include <cassert>

int metaFibonacciSum(int n)
{
    if (n < 2) {
        return n;
    }

    int terms[n] = {0, 1};

    for (int index = 2; index < n + 1; index++) {
        terms[index] = terms[index - 1] + terms[index - 2];
    }
    
    int partialSums[terms[n]] = {0};

    for (int i = 1; i < terms[n] + 1; i++) {
        if (i <= n ) {
            partialSums[i] = partialSums[i-1] + terms[i];
        }
        else {
            partialSums[i] = partialSums[i-1] + partialSums[i-2] + 1;
        }
    }

    int sum = 0;

    for (int k = 0 ; k < n + 1; k++) {
        sum = sum + partialSums[terms[k]];
    }
    return sum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6) == 74);

    std::cout << "Success!";

    return 0;
}