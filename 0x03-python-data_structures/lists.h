#ifndef LISTS_H
#define LISTS_H
#include <Python.h>

#include <Python.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
void print_list_integer(int *my_list, int size);
int element_at(int *my_list, int idx);
int replace_in_list(int *my_list, int idx, int new_element);
void print_reversed_list_integer(int *my_list, int size);
int *new_in_list(int *my_list, int idx, int new_element);
char *no_c(char *str);
void print_matrix_integer(int **matrix, int rows, int cols);
int *add_tuple(int *tuple_a, int *tuple_b);
struct multiple_returns multiple_returns(char *sentence);
int max_integer(int *my_list, int size);
int *divisible_by_2(int *array, int size);
void delete_at(int **array, unsigned int idx);
void switch_elements(int **array, unsigned int idx_a, unsigned int idx_b);
listint_t *insert_node(listint_t **head, int number);
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n);
int delete_nodeint_at_index(listint_t **head, unsigned int index);
void reverse_listint(listint_t **head);
void print_python_list_info(PyObject *p);
#endif /* LISTS_H */
