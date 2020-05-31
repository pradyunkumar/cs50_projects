#include <stdio.h>
#include <stdlib.h>

//represents a node
typedef struct node
{
    int number; //number
    struct node *next;  //pointer to next
}
node;

int main(void)
{
    //List of size 0
    node *list = NULL;
    
    //add number to list
    node *n = malloc(sizeof(node));
    if (n != NULL)
    {
        return 1;
    }
    n->number = 1;  //allocates number field in node to 1
    n->next = NULL; //pointer is initially NULL
    list = n;   //starting pointer is to 1
    
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    list->next = n; //connects the code
    
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n; //connects the code
    
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp-> number);
    }
    
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
}