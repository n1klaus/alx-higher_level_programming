#include "lists.h"
/**
 * check_cycle - check if there are cycles available
 * @list: list node
 *
 * Return: 0 if there is no cycle;
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (list != NULL)
	{
		list = list->next;
		if (head == list)
			return (1);
	}
	return (0);
}
