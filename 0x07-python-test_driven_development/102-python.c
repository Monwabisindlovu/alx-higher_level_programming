#include <Python.h>
#include <locale.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	setlocale(LC_ALL, "");
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	len = PyUnicode_GET_LENGTH(p);
	PyUnicode_READY(p);
	str = PyUnicode_AsWideCharString(p, &len);
	printf("[.] string object info\n");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else if (PyUnicode_IS_COMPACT(p))
		printf("  type: compact unicode object\n");
	else
		printf("  type: compact not ascii\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}



