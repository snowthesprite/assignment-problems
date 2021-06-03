# include <iostream>
# include <cassert>

int sum_cube(int max){
    int sum = 0;

    for (int num = 1; num <= max; num ++){
        sum += num * num * num;
    }
    return sum;
}

int main() {
    int cube = sum_cube(10);


    std::cout << cube;

    return 0;
}