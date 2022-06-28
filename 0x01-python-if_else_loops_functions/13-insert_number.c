#include "lists.h"
/**
 * insert_node - add a node at the end of a singly linked list
 * @head: head node
 * @number: integer value
 *
 * Return: pointer to a node structure or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = NULL;

	new = malloc(sizeof(listint_t) * 100);
	if (new == NULL)
		return (NULL);
	
	if (*head == NULL)
		*head = malloc(sizeof(listint_t) * 100);
	temp = *head;

	while (temp != NULL)
		temp = temp->next;

	temp->next = new;
	new->n = number;
	return (new);
}
