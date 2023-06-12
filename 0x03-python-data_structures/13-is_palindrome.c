#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"

void reverse_list(listint_t **prev, listint_t **next, listint_t **rev);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *rev = NULL, *fast, *prev = NULL, *next, *prev_next;
	int len = 0, i = 0, odd = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	slow = *head;
	fast = *head;
	while (fast && fast->next)
	{
		len++;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		odd = 1;
	rev = *head;
	while (i < len)
	{
		next = rev->next;
		rev->next = prev;
		prev = rev;
		rev = next;
		i++;
	}
	prev_next = prev;
	if (odd == 1)
		next = next->next;
	while (prev_next && next)
	{
		if (prev_next->n != next->n)
		{
			next = NULL;
			reverse_list(&prev, &next, &rev);
			return (0);
		}
		prev_next = prev_next->next;
		next = next->next;
		i++;
	}
	reverse_list(&prev, &next, &rev);
	return (1);
}

/**
 * reverse_list - reverse list
 * @prev: pointer
 * @next: pointer
 * @rev: pointer
 */

void reverse_list(listint_t **prev, listint_t **next, listint_t **rev)
{
	while (*prev)
	{
		*next = (*prev)->next;
		(*prev)->next = *rev;
		*rev = *prev;
		*prev = *next;
	}
}

