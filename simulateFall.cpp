#include <iostream>
#include "constants.h"

double calculateDistanceFallen(int seconds)
{
    // approximate distance fallen after a particular number of seconds
    double distanceFallen = myConstants::gravity * seconds * seconds / 2;

    return distanceFallen;
}

void printStatus(int time, double height)
{
    std::cout << "At " << time
    << " seconds, the ball is at height "
    << height << " meters\n";
}

int main()
{
    using namespace std;
    cout << "Enter the initial height of the tower in meters: ";
    double initialHeight;
    cin >> initialHeight;
    double height = initialHeight;
    int seconds = 0;
    while (height > 0) {
        height = initialHeight - calculateDistanceFallen(seconds);
        if (height < 0) {
            height = 0;
        }
        printStatus(seconds, height);
        seconds = seconds + 1;
    }

    // your code here
    // use calculateDistanceFallen to find the height now

    // use calculateDistanceFallen and printStatus
    // to generate the desired output
    // if the height now goes negative, then the status
    // should say that the height is 0 and the program
    // should stop (since the ball stops falling at height 0)

    return 0;
}