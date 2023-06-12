#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"

listint_t *push(listint_t **head, int n);
int pop(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *rev = NULL, *fast;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	slow = *head;
	fast = *head;

	while (fast && fast->next)
	{
		push(&rev, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	while (rev && slow)
	{
		if (pop(&rev) != slow->n)
		{
			while (rev)
			{
				fast = rev->next;
				free(rev);
				rev = fast;
			}
			return (0);
		}
		slow = slow->next;
	}

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

/**
 * pop - delete node from start
 * @head: the head of the node
 *
 * Return: the data in the node
 */

int pop(listint_t **head)
{
	listint_t *temp;
	int n;

	temp = *head;
	*head = (*head)->next;
	n = temp->n;
	free(temp);
	return (n);
}

