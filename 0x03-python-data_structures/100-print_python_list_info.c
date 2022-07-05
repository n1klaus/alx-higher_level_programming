#include "libpylist.h"

/**
 * PyList_Check - check if an object is a listint_t list
 * @p : pointer to a python object
 * 
 * Return : 0 if successful; 1 otherwise
 */
int PyList_Check(PyObject *p)
{
	if (sizeof(p) / sizeof(p[0]) > 1)
	{
		while (p++)
		{
			p->ob_size++;
			p->ob_type = Py_TYPE(p);
			p->ob_refcnt++;
		}
		return (0);
	}
	else
		return (1);
}

/**
 * print_python_list_info - print information about a python list
 * @p : pointer to a python object 
 * 
 * Return : Nothing
 */
void print_python_list_info(PyObject *p)
{
	size_t index = 0, len;

	if ((PyList_Check(p)) != 0)
		exit(1);
	len = p->ob_size;
	printf("[*] Size of the Python List = %s\n", p->ob_size);
	printf("[*] Allocated = %s\n", p->ob_refcnt);

	while(len--)
	{
		printf("Element %d: %s\n", index, Py_TYPE(p[index]));
		index++;
	}
}