#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer
 */

void print_python_list_info(PyObject *p)
{
	int len, i;
	char *type;

	if (!PyList_Check(p))
		return;

	len = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		type = Py_Type(((PyListObject *)p)->ob_item[i]->tp_name);
		printf("Element %d: %s", i, type);
	}
}

