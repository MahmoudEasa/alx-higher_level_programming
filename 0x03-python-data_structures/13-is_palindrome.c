#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

listint_t *push(listint_t **head, int n);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *rev = NULL, *current_rev;

	if (!head || !(*head))
		return (1);

	current = *head;

	while (current)
	{
		push(&rev, current->n);
		current = current->next;
	}

	current = *head;
	current_rev = rev;

	while ((current && current_rev))
	{
		if (current->n != current_rev->n)
		{
			free_listint(rev);
			return (0);
		}
		current = current->next;
		current_rev = current_rev->next;
	}

	free_listint(rev);

	return (1);
}

/**
 * push - add node to start
 * @head: the head of the node
 * @n: intger
 *
 * Return: pointer to new node
 */

listint_t *push(listint_t **head, int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

