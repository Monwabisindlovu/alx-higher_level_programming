#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_GET_SIZE(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GET_ITEM(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
char *str;
Py_ssize_t size, i;

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

str = PyBytes_AS_STRING(p);
size = PyBytes_GET_SIZE(p);
printf("[.] bytes object info\n");
printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);
printf("  first %zd bytes: ", size < 10 ? size + 1 : 10);

for (i = 0; i < size + 1 && i < 10; i++)
{
printf("%02hhx ", str[i]);
}
printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
double value;

if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AS_DOUBLE(p);
printf("[.] float object info\n");
printf("  value: %g\n", value);
}

