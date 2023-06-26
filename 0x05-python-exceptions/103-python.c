#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <float.h>
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/bytesobject.h"
#include "/usr/include/python3.4/floatobject.h"

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Python lists
 * @p: PyListObject
 */

void print_python_list(PyObject *p)
{
	const char *type;
	PyObject *item;
	size_t i, len;

	fflush(stdout);

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
			else if (strcmp(type, "float") == 0)
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes - Python bytes
 * @p: PyBytesObject
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	int i, len;

	fflush(stdout);

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
		{
			printf("%02x", (unsigned char)str[i]);
			if (i < len)
				printf(" ");
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_float - Python float
 * @p: PyFloatObject
 */

void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	fflush(stdout);

	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		buffer = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval, 'r', 0,
				Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buffer);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

