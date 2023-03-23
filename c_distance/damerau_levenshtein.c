#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

// This is a 1:1 translation of https://github.com/jamesturk/jellyfish/blob/main/jellyfish/_jellyfish.py

int min_int(int arr[], size_t size)
{
    // simply loop over an array of integers to find the min
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
    const unsigned char* s1;
    const unsigned char* s2;

    if ( !PyArg_ParseTuple(args, "ss", &s1, &s2) ) // s means string argument
    {
        return NULL;
    }

    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    size_t infinite = len1 + len2;

    size_t nrows = len1 + 2;
    size_t ncols = len2 + 2;

    // initialize distance matrix
    int score[nrows][ncols];
    memset(score, 0, sizeof(score[0][0] * nrows * ncols));

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
    
    // Since we are only dealing with ascii characters, this is equivalent to the dictionary
    // in the Python implementation. Instead of accessing using the character as the index, we
    // can cast the character to its integer version, and access by index.
    int da[256];
    memset(da, 0, sizeof(da));

    for (size_t i = 1; i <= len1; i++)
    {
        int db = 0;
        for (size_t j = 1; j <= len2; j++)
        {
            const unsigned char s2_char = s2[j - 1];
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
        const unsigned char s1_char = s1[i - 1];
        da[(size_t)s1_char] = i;
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
