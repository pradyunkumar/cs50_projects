#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[4];
    
    people[0].name = "EMMA";
    people[0].number = "617-555-0100"
    
    people[1].name = "RODRIGO";
    people[1].number = "617-555-0101";
    
    for (int i = 0; i < 4; i++)
    {
        if(strcmp("dog", string[i]) == 0)
        {
            printf("Found\n");
        }
    }
    printf("Not Found\n");
}