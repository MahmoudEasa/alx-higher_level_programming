#include "lists.h"
#include <stdlib.h>

void push(listint_t *new, listint_t *ptr);
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
	if (!(*head) || (*head)->n > number)
	{
		new->next = *head;
		(*head) = new;
	}
	else
	{
		ptr = (*head);
		while (ptr->next)
		{
			if (ptr->next->n > number)
			{
				push(new, ptr);
				break;
			}
			ptr = ptr->next;
		}

		if (!ptr->next)
			push(new, ptr);
	}
	return (new);
}

/**
 * push - add node
 * @new: pointer to new node
 * @ptr: pointer to the index to add the Node
 */

void push(listint_t *new, listint_t *ptr)
{
	new->next = ptr->next;
	ptr->next = new;
}
