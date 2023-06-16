#include <Python.h>
#include <stdio.h>
#include "/usr/include/python3.4/bytesobject.h"

void print_python_bytes(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists
 * @p: PyObject Pointer
 */

void print_python_list(PyObject *p)
{
	const char *type;
	PyObject *item;
	size_t i, len;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		len = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", len);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < len; i++)
		{
			item = PyList_GET_ITEM(p, i);
			type = item->ob_type->tp_name;
			printf("Element %ld: %s\n", i, type);
			if (strcmp(type, "bytes") == 0)
				print_python_bytes(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: PyObject Pointer
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	int i, len;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		str = PyBytes_AsString(p);
		len = PyBytes_Size(p);
		printf("  size: %d\n", len);
		printf("  trying string: %s\n", str);
		if (len > 10)
			len = 9;
		printf("  first %d bytes: ", (len + 1));
		for (i = 0; i <= len; i++)
			printf("%02x ", (unsigned char)str[i]);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

