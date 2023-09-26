#include <Python.h>
#include <stdio.h>

void print_python_float(PyObject *p);

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size, i;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
printf("  size: %zd\n", size);
printf("  trying string: %s\n", bytes->ob_sval);

if (size > 10)
size = 10;
else
size++;

printf("  first %zd bytes: ", size);

for (i = 0; i < size; i++)
{
printf("%02x", bytes->ob_sval[i] & 0xff);
if (i + 1 < size)
printf(" ");
}
printf("\n");
}

/**
 * print_python_list - Prints information about Python list objects
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, i;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", list->allocated);

for (i = 0; i < size; i++)
{
PyObject *item = list->ob_item[i];
printf("Element %zd: ", i);

if (PyBytes_Check(item))
print_python_bytes(item);
else if (PyFloat_Check(item))
print_python_float(item);
else
printf("%s\n", Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
PyFloatObject *f = (PyFloatObject *)p;
double value = f->ob_fval;

printf("[.] float object info\n");
printf("  value: %f\n", value);
}

