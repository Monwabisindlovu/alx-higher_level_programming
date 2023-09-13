fndef LISTS_H
#define LISTS_H

/* Task 0 */
int square_matrix_simple(int **matrix, int rows, int cols);

/* Task 1 */
int *search_replace(int *my_list, int size, int search, int replace);

/* Task 2 */
int uniq_add(int *my_list, int size);

/* Task 3 */
set_t *common_elements(set_t *set_1, set_t *set_2);

/* Task 4 */
set_t *only_diff_elements(set_t *set_1, set_t *set_2);

/* Task 5 */
int number_keys(dictionary_t *a_dictionary);

/* Task 6 */
void print_sorted_dictionary(dictionary_t *a_dictionary);

/* Task 7 */
dictionary_t *update_dictionary(dictionary_t *a_dictionary, const char *key, const char *value);

/* Task 8 */
int simple_delete(dictionary_t *a_dictionary, const char *key);

/* Task 9 */
dictionary_t *multiply_by_2(dictionary_t *a_dictionary);

/* Task 10 */
char *best_score(dictionary_t *a_dictionary);

/* Task 11 */
int *multiply_list_map(int *my_list, int size, int number);

/* Task 12 */
int roman_to_int(const char *roman_string);

/* Task 13 */
float weight_average(int *my_list, float *weights, int size);

/* Task 14 */
int **square_matrix_map(int **matrix, int size);

/* Task 15 */
void complex_delete(dictionary_t *a_dictionary, int value);

/* Task 16 */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

#endif /* LISTS_H */

