#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the node
 * @number: integer
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(new));
	if (!new)
		return (NULL);

	new->n = number;
	if (!(*head))
	{
		new->next = NULL;
		(*head) = new;
	}
	else
	{
		ptr = (*head);
		while (ptr->next)
		{
			if (ptr->next->n > number)
			{
				new->next = ptr->next;
				ptr->next = new;
				break;
			}
			ptr = ptr->next;
		}

		if (!ptr->next)
		{
			new->next = ptr->next;
			ptr->next = new;
		}
	}
	return (new);
}
