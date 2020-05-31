#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>


unsigned int hash(const char *word)
{
    int hash = 0;
    int ind = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (i <= 3)
        {
            if (word[i] == 39)
            {
                hash += 1;
            }
            else
            {
                if (islower(word[i]))
                {
                    ind = 97;
                }         
    
                else 
                {
                    ind = 65;
                }
                
                hash += ((int)pow(26, 3 - i)) * ((int) word[i] - ind);
            }
        }
    }
    return hash;
}

unsigned int hash(const char *str)
{
    unsigned int hash = 5381;
    int c;
    int count = 0;

    while ((c = tolower(*str++)) && count < 3)
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
        count++;
    }
    
    return hash;
}
    
int main(void)
{
    // string s = get_string("Input: ");
    // printf("Output: ");
    // // int length = strlen(s);
    // for (int i = 0, n = strlen(s); i < n; i++)
    // {
    //     printf("%c", toupper(s[i]));
    // }
    // printf("\n");
    char *input = malloc(sizeof(char *));
    while (strcmp(input, "quit"))
    {
        printf("Please enter a word: ");
        scanf("%s", input);
        printf("hash: %i\n", hashs(input));
    }
    free(input);

}


