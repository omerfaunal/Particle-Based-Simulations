#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h> 

// Randomly select x and theta
// Check if needle crosses a line which is if right side of needle is greater than D or left side is smaller than 0
bool throw_needle(double D, double L) {
    double x = ((double)rand() / RAND_MAX) * D / 2;
    double theta = ((double)rand() / RAND_MAX) * M_PI / 2;

    return (x <= L / 2.0 * sin(theta));
}

// Throws needle experiment_count times and calculates the collision count
// Calculates the probability of collision and pi
void experiment(int experiment_count, int D, int L) {
    int collision = 0;
    for(int i = 0; i < experiment_count; i++) {
        if(throw_needle(D, L)) {
            collision++;
        }
    }

    double probabilty = (double)collision / (double)experiment_count;
    double pi = (2.0 * L) / (D * probabilty);
    printf("ExperimentCount: %d \nD: %d, L: %d, P: %f, PI: %f\n",experiment_count, D, L, probabilty, pi);
}

int main(int argc, char *argv[]) {
    srand(time(NULL));
    if (argc != 4) {
        printf("Usage: ./simulation <experiment_count> <D> <L>\nIf experiment count is 0 it will run for all 10^x: 2 <= x <= 6 \n");
        return 1;
    }
    if (atoi(argv[3]) > atoi(argv[2])) {
        printf("L must be smaller than D\n");
        return 1;
    }
    if (atoi(argv[1]) == 0) {
        int experiment_counts[] = {pow(10,2), pow(10,3), pow(10, 4), pow(10,5), pow(10,6)};
        for(int i = 0; i < 5; i++) {
            experiment(experiment_counts[i], atoi(argv[2]), atoi(argv[3]));
        }
        return 0;
    } else {
        experiment(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));
    }

    
    return 0;
}



