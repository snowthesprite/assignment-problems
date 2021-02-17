# include <iostream>
# include <cassert>

int main()
{
    int array[5]{ 30, 50, 20, 10, 40 };

    for (int i = 0; i <= 5; i++) {
        int element1 = array[i];
        for (int k = 0 + i; k <= 5; k++){
            int element2 = array[k];
            if (element2 < element1) {
                array[i] = element2;
                array[k] = element1;
                element1 = element2;
            }
        }
    }

    std::cout << "Testing...\n";

    assert(array[0]==10);
    assert(array[1]==20);
    assert(array[2]==30);
    assert(array[3]==40);
    assert(array[4]==50);

    std::cout << "Succeeded";

    return 0;
}