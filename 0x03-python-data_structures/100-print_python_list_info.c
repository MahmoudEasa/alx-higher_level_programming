#include <Python.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer
 */

void print_python_list_info(PyObject *p)
{
	size_t len, i;
	const char *type;

	len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", (signed long)((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		type = Py_Type(((PyListObject *)p)->ob_item[i]->tp_name);
		printf("Element %ld: %s\n", i, type);
	}
}

