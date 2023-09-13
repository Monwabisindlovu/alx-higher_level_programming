#include <Python.h>
#include "lists.h"

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list(PyObject *p)
{
long int size, i;
const char *type;

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
type = ((PyListObject *)p)->ob_item[i]->ob_type->tp_name;
printf("Element %ld: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(((PyListObject *)p)->ob_item[i]);
}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: A PyObject bytes object.
 */
void print_python_bytes(PyObject *p)
{
unsigned char *str;
Py_ssize_t size;
long int i;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = (unsigned char *)PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

if (size < 10)
printf("  first %ld bytes:", size + 1);
else
printf("  first 10 bytes:");

for (i = 0; i <= size && i < 10; i++)
printf(" %02hhx", str[i]);

printf("\n");
}
