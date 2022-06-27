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
	if (list->next == NULL)
		return (0);
	check_cycle(list->next);
	return (1);
}
