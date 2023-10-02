#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <Python.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *second = NULL;
    int result = 1;

    if (head == NULL || *head == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    second = slow;
    prev->next = NULL;

    second = reverse_list(second);

    result = compare_lists(*head, second);

    second = reverse_list(second);

    prev->next = second;

    return (result);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the first node of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * compare_lists - compares two singly linked lists
 * @head1: pointer to the first node of the first list
 * @head2: pointer to the first node of the second list
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }

    if (head1 == NULL && head2 == NULL)
        return (1);

    return (0);
}

