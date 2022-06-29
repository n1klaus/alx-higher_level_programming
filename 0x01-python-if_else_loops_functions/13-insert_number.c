#include "lists.h"
/**
 * insert_node - add a number in a sorted singly linked list
 * from smallest number to the largest
 * @head: head node
 * @number: integer value to add
 *
 * Return: pointer to a node structure or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	int c_num = (*head)->n;
	listint_t *temp = NULL, *curr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	if (number <= c_num)
	{
		temp = *head;
		new->n = number;
		new->next = temp;
		*head = new;
	}
	else
	{
		while (curr != NULL)
		{
			temp = curr;
			curr = curr->next;
			if (curr == NULL)
				break;
			c_num = curr->n;
			if (c_num > number)
				break;
		}
		temp->next = new;
		new->n = number;
		if (curr == NULL)
			new->next = NULL;
		else
			new->next = curr;
	}
	return (new);
}
