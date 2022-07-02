#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : pointer to the pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head);
{
    listint_t *current = NULL;
    int i = 0, j, *store = malloc(sizeof(int) * BUFSIZ);

    if (*head == NULL)
        return (1);
    
    current  = *head;
    for (; current != NULL; store++)
    {
        *store = current->n;
        current = current->next;
    }

    j = len(store) - 1;
    while(store-- && (j != j / 2))
    {
        if (store[i++] == store[j--])
            continue;
        else
            return (0);
    }
    free(store);
    return (1);
}