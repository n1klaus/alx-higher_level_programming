#ifndef __LIBPYLIST_H__
#define __LIBPYLIST_H__

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <object.h>
#include <listobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif /* __LIBPYLIST_H__*/