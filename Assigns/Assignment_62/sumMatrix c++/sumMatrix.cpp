#include <iostream>
#include <cassert>

int calcSum (int m, int n) {
    int asc[2][3];
    int desc[3][2];
    int sumArr[2][2];
    int max = 2 * 3;
    int sum = 0;

    for (int i = 0; i < 2; i++) {
        for (int k = 0; k < 3; k++) {
            asc[i][k] = (i*3) + k + 1;
        }
    }
    for (int m = 0; m < 3; m++) {
        for (int n = 0; n < 2; n++) {
            desc[m][n] = max - (m*2) - n;
        }
    }
    for (int a = 0; a < 2; a++) {
        for (int a2 = 0; a2 < 2; a2++){    
            for (int b = 0; b < 3; b++) {
                sum = sum + asc[a][b] * desc[b][a2];
            }
        }
    }

    return sum;
}

int main() {
    std::cout << "Testing...\n";

    assert(calcSum(2,3) == 131);

    std::cout << "Succeeded";

    return 0;
}