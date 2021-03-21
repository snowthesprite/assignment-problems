# include <iostream>
# include <cassert>

void calcSum (int *row1, int *row2, int *rowSum, int numCols) {
    for (int index = 0; index < numCols; index++){
        rowSum[index] = row1[index] + row2[index];
    }
}

int main() {
    std::cout << "Testing...\n";

    int matrix[2][3] = {
        { 1, 2, 3 },
        { 4, 5, 6 }
    };

    int numRows = sizeof(matrix)/sizeof(matrix[0]);
    int numCols = sizeof(matrix[0])/sizeof(matrix[0][0]);
    // I think thats general?

    assert(numRows == 2);
    assert(numCols == 3);

    int rowSum[numCols];
    calcSum(matrix[0], matrix[1], rowSum, numCols);

    assert(rowSum[0] == 5);
    assert(rowSum[1] == 7);
    assert(rowSum[2] == 9);

    std::cout << "Success!";

    return 0;
}