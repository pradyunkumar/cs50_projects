#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string input = get_string("Text: ");
    int askiinum;
    int totletters = 0;
    int totwords = 0;
    int totsentences = 0;
    
    for (int i = 0, n = strlen(input); i <= n; i++)
    {
        askiinum = (int)input[i];
        if ((askiinum >= 65 && askiinum <= 90) || 
            (askiinum >= 97 && askiinum <= 122))
        {
            totletters++;
        }
        else if (askiinum == 32 || askiinum == 0)
        {
            totwords++;
        }
        else if (askiinum == 33 || askiinum == 46 || askiinum == 63)
        {
            totsentences++;
        }
    }
    
    double index = (0.0588 * (totletters / (double)totwords * 100)) -
                   (0.296 * (totsentences / (double)totwords * 100)) - 15.8;
                
    // printf("%i letter(s)\n", totletters);
    // printf("%i word(s)\n", totwords);
    // printf("%i sentence(s)\n", totsentences);
    
    if (index < 1)
    {
        printf("Before Grade 1");
    }
    else if (index > 16)
    {
        printf("Grade 16+");
    }
    else 
    {
        printf("Grade %i", (int)round(index));
    }
    
    printf("\n");
}