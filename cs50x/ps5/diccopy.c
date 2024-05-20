// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Initialize Count of words int.
int nofw = 0;


// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return (toupper(word[0]) - 'A');
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    for (int i = 0; i < N; i++)
{
    table[i] = NULL;
}
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    while (true)
    {
        char *fout = malloc((LENGTH + 1) * sizeof(char));
        if (fscanf(source, "%s", fout) == 1)
        {
            node *n = malloc(sizeof(node));
            strcpy(n->word, fout);
            unsigned int hash_value = hash(n->word);
            n->next = table[hash_value];
            table[hash_value] = n;
            nofw++;
            free(fout);
        }
        else
        {
            return false;
        }
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return nofw;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
