#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the node
 * @number: integer
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(new_node) * 2);
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!(*head) || (*head)->n > number)
	{
		new_node->next = *head;
		(*head) = new_node;
	}
	else
	{
		ptr = (*head);
		while (ptr->next)
		{
			if (ptr->next->n > number)
			{
				push(new_node, ptr);
				break;
			}
			ptr = ptr->next;
		}

		if (!ptr->next)
			push(new_node, ptr);
	}
	return (new_node);
}

/**
 * push - add node
 * @new_node: pointer to new node
 * @ptr: pointer to the index to add the Node
 */

void push(listint_t *new_node, listint_t *ptr)
{
	new_node->next = ptr->next;
	ptr->next = new_node;
}
