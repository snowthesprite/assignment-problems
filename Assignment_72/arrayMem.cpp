# include <iostream>
# include <cassert>

int main() {

    int array[4] = { 11, 12, 13, 14 };

    std::cout << "Array has address: " << &array << "\n";
    for (int index = 0; index < 4; index++){
        std::cout << "Index " << index << " has value " << array[index] << " and adress "<< & array[index] << "\n";
    }

    return 0;
}