#include <stdio.h>
#include <cs50.h>

//const int N = 3;
float average(int length, int array[]);

int main(void)
{
    int n = get_int("Number of Scores: ");
    int scores[n];
    
    for(int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score %i: ", i+1);
    }
    
    printf("Average: %0.1f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for(int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return ((float) sum/ (float)length);
}