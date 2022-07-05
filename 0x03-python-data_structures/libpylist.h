#ifndef __LIBPYLIST_H__
#define __LIBPYLIST_H__

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define Py_TYPE(expr) \
    (_Generic((expr), \
              char: "char", unsigned char: "unsigned char",\
			  signed char: "signed char",\
              short: "short", unsigned short: "unsigned short",\
              int: "int", unsigned int: "unsigned int",\
              long: "long", unsigned long: "unsigned long",\
              long long: "long long", unsigned long long: "unsigned long long",\
              float: "float", \
              double: "double", \
              long double: "long double", \
              void*: "void*", \
              default: "?")) 

/**
 * struct pyTypeObject - python list object
 * @ob_refcnt: object reference count
 * @ob_type: object data type
 * @ob_size : object length size
 * 
 * Description: singly linked list node structure
 * for interacting with python objects
 */
typedef struct pyTypeObject{
    typedef ssize_t ob_refcnt;
    typedef char* ob_type;
	typedef size_t ob_size;
}PyListObject;

int PyList_Check(PyListObject *p);
void print_python_list_info(PyListObject *p);

#endif /* __LIBPYLIST_H__*/