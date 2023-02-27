#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

int min_int(int arr[], size_t size)
{
    int min = arr[0];
    for (size_t i = 1; i < size; i++)
    {
        int val = arr[i];
        if (val < min)
        {
            min = val;
        }
    }
    
    return min;
}

static PyObject* distance(PyObject *self, PyObject *args)
{
    const char* s1;
    const char* s2;

    if ( !PyArg_ParseTuple(args, "ss", &s1, &s2) )
    {
        return NULL;
    }

    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int infinite = len1 + len2;

    int nrows = len1 + 2;
    int ncols = len2 + 2;

    int score[nrows][ncols];
    for (size_t i = 0; i < nrows; i++)
    {
        for (size_t j = 0; j < ncols; j++)
        {
            score[i][j] = 0;
        }
    }

    score[0][0] = infinite;
    for (size_t i = 0; i <= len1; i++)
    {
        score[i + 1][0] = infinite;
        score[i + 1][1] = i;
    }
    for (size_t i = 0; i <= len2; i++)
    {
        score[0][i + 1] = infinite;
        score[1][i + 1] = i;
    }
    
    int da[256] = { 0 };
    for (size_t i = 1; i <= len1; i++)
    {
        int db = 0;
        for (size_t j = 1; j <= len2; j++)
        {
            const char s2_char = s2[j - 1];
            int i1 = da[(int)s2_char];
            int j1 = db;
            int cost = 1;
            if (s1[i - 1] == s2_char)
            {
                cost = 0;
                db = j;
            }
            
            int arr[4] = {
                score[i][j] + cost,
                score[i + 1][j] + 1,
                score[i][j + 1] + 1,
                score[i1][j1] + (i - i1 - 1) + 1 + (j - j1 - 1)
            };
            score[i + 1][j + 1] = min_int(arr, 4);
        }
        const char s1_char = s1[i - 1];
        da[(int)s1_char] = i;
    }
        
    long distance = score[len1 + 1][len2 + 1];

    return PyLong_FromLong(distance);
}

static struct PyMethodDef methods[] =
{
    {"distance", (PyCFunction)distance, METH_VARARGS},
    {NULL, NULL, NULL}
};

static struct PyModuleDef module = 
{
    PyModuleDef_HEAD_INIT,
    "_damerau_levenshtein",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__damerau_levenshtein(void)
{
    return PyModule_Create(&module);
}
