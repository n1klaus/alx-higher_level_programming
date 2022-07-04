#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : pointer to the pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int l = 0, c = 1, u = 0, t = 1, *store = malloc(BUFSIZ);

	if (*head == NULL)
		return (1);

	current  = *head;
	*store = current->n;

	for (; current != NULL; t++)
	{
		current = current->next;
		if (current != NULL)
		{
			store[t] = current->n;
			c++;
		}
	}

	if (c % 2 == 0)
	{
		l = c / 2 - 1;
		u = c / 2;
	}
	else
	{
		l = c / 2 - 1;
		u = c / 2 + 1;
	}

	while (l >= 0 && u <= c)
	{
		if (store[l--] != store[u++])
			return (0);
	}
	free(store);
	return (1);
}
