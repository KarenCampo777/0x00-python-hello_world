#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is not.
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (list && tmp)
	{
		tmp = tmp->next;
		if (tmp == list)
			return (1);
		if (tmp == NULL)
			return (0);
		list = list->next;
		tmp = tmp->next;
	}
	return (0);
}
