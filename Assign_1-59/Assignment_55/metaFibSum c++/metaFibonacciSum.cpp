# include <iostream>
# include <cassert>

int metaFibonacciSum(int n)
{
    int fibArray[n] = {0, 1};

    for (int index = 2; index <= n ; index++) {
        fibArray[index] = fibArray[index - 1] + fibArray[index - 2];
    }
    
    int fibSumArray[fibArray[n]] = {0};

    for (int i = 1; i <= fibArray[n]; i++) {
        if (i <= n ) {
            fibSumArray[i] = fibSumArray[i-1] + fibArray[i];
        }
        else {
            fibSumArray[i] = fibSumArray[i-1] + fibSumArray[i-2] + 1;
        }
    }

    int fibSum = 0;

    for (int k = 0 ; k <= n; k++) {
        fibSum = fibSum + fibSumArray[fibArray[k]];
    }
    return fibSum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6) == 74);

    std::cout << "Success!";

    return 0;
}