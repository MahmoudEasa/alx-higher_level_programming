#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the head of nodes
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *next;

	if (!list || !(list->next))
		return (0);

	next = list->next;

	while (current && next)
	{
		if (current == next)
			return (1);

		current = current->next;
		if (next->next && next->next->next)
			next = next->next->next;
		else
			return (0);
	}
	return (0);
}

