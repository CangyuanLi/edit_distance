#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

static PyObject* distance(PyObject *self, PyObject *args)
{
    const char* s1;
    const char* s2;

    if ( !PyArg_ParseTuple(args, "ss", &s1, &s2) ) // unicode
    {
        return NULL;
    }

    if ( strlen(s2) > strlen(s1) )
    {
        const char* tmp = s1;
        s1 = s2;
        s2 = tmp;
    }

    int s1_len = strlen(s1);
    int s2_len = strlen(s2);
    long dist = s1_len - s2_len;
    for (size_t i = 0; i < s2_len; i++)
    {
        if (s1[i] != s2[i])
        {
            dist += 1;
        }
    }
    
    return PyLong_FromLong(dist);
}

static struct PyMethodDef methods[] =
{
    {"distance", (PyCFunction)distance, METH_VARARGS},
    {NULL, NULL, NULL}
};

static struct PyModuleDef module = 
{
    PyModuleDef_HEAD_INIT,
    "_hamming",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__hamming(void)
{
    return PyModule_Create(&module);
}
