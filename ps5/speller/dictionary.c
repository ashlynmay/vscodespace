// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Initialize an integer for the word count
int wc = 0;
int hashvalue;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (strlen(word) >= 3)
    {
        int upper1 = toupper(word[0]) - 'A';
        int upper2 = toupper(word[1]) - 'A';
        int upper3 = toupper(word[2]) - 'A';
        return ((upper1 * pow(26, 2)) + (upper2 * pow(26, 1)) + (upper3 * pow(26, 0)));
    }

    else if (strlen(word) == 2)
    {
        int upper1 = toupper(word[0]) - 'A';
        int upper2 = toupper(word[1]) - 'A';
        return ((upper1 * pow(26, 1)) + (upper2 * pow(26, 0)));
    }

    else if (strlen(word) == 1)
    {
        int upper1 = toupper(word[0]) - 'A';
        return ((upper1 * pow(26, 0)));
    }

    else
    {
        return 0;
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char read[LENGTH + 1];

    while (fscanf(file, "%s", read) != EOF)
    {
        wc++;
        // Create node per new word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        else
        {
            // Copy read word to new node
            strcpy(n->word, read);
            hashvalue = hash(read);
            n->next = table[hashvalue];
            table[hashvalue] = n;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wc;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
