# include <iostream>
# include <cassert>

int seqSum (int n) 
{
    int sumArray [n] = {0, 1};

    for (int index = 2; index <= n ; index++) {
        sumArray[index] = sumArray[index - 1] + 2 * sumArray[index - 2];
    }

    int sum = 0;

    for (int index = 0; index <= n ; index++) {
        sum = sum + sumArray[index];
    }

    return sum;
}

int extendedSeqSum (int n)
{
    int startSumArray [n] = {0, 1};

    for (int index = 2; index < n ; index++) {
        startSumArray[index] = startSumArray[index - 1] + 2 * startSumArray[index - 2];
    }

    int startSum = 0;

    for (int index = 0; index < n ; index++) {
        startSum = startSum + startSumArray[index];
    }

    int sumArray[startSum] = {};
    
    for (int index = 0; index <= n ; index++) {
        sumArray[index] = startSumArray[index];
    }

    for (int index = n; index <= startSum ; index++) {
        sumArray[index] = sumArray[index - 1] + 2 * sumArray[index - 2];
    }

    int sum = startSum;

    for (int index = n; index <= startSum ; index++) {
        sum = sum + sumArray[index];
    }

    return sum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}