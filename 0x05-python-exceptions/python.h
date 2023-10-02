#ifndef PYTHON_H
#define PYTHON_H

#include <Python.h>
typedef struct _object PyObject;
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);


#endif /* PYTHON_H */
