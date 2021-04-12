# include <iostream>
# include <cassert>

int calcIndex (int n) {
    int fibArray[n] = {0, 1};
    for (int index = 2; index < n; index ++) {
        fibArray[index] = fibArray[index - 1] + fibArray[index - 2];
        if (fibArray[index] > n) {
            return index;
        }
    }
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}