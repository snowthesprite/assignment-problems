# include <iostream>
# include <cassert>

int dotProduct (int *arr1, int *arr2, int length) {
    int sum = 0;
    for (int index = 0; index < length; index++){
        sum += arr1[index] * arr2[index];
    }
    return sum;
}

int main()
{

    int array1[] = {1, 2, 3, 4};
    int array2[] = {5, 6, 7, 8};
    int length = sizeof(array1) / sizeof(array1[0]);
    int ans = dotProduct(array1, array2, length);

    std::cout << "Testing...\n";
    assert(ans == 70);
    std::cout << "Success!";

    return 0;
}