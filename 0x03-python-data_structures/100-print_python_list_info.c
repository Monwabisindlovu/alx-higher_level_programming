#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
<<<<<<< HEAD
#include "lists.h"
=======

>>>>>>> 1aab2a969293e50d8deed46f1be432b502d0f595
/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
<<<<<<< HEAD
    Py_ssize_t size, alloc, i;
    PyObject *item;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);

        item = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(item)->tp_name);
    }
=======
Py_ssize_t size, alloc, i;
PyObject *item;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
printf("Element %ld: ", i);

item = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(item)->tp_name);
}
>>>>>>> 1aab2a969293e50d8deed46f1be432b502d0f595
}

