#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int letters(string input);
int words(string input);
int sentences(string input);
int formulate(float l, float w, float s);

int lcount = 0;
int wcount = 1;
int scount = 0;

int main(void)
{
    string input = get_string("Text: ");
    letters(input);
    words(input);
    sentences(input);
    formulate(lcount, wcount, scount);
}

// Calculate amount of letters per input.
int letters(string input)
{
    for (int i = 0, len = strlen(input); i <= len; i++)
    {
        if (isalpha(input[i]))
        {
            lcount++;
        }
    }
    // printf("Letter count: %d\n", lcount);
    return lcount;
}

// Calculate amount of words per input.
int words(string input)
{
    for (int i = 0, len = strlen(input); i <= len; i++)
    {
        if (isspace(input[i]))
        {
            wcount++;
        }
    }
    // printf("Word count: %d\n", wcount);
    return wcount;
}

// Calculate amount of sentences per input.
int sentences(string input)
{
    for (int i = 0, len = strlen(input); i <= len; i++)
    {
        if (input[i] == '.' || input[i] == '!' || input[i] == '?')
        {
            scount++;
        }
    }
    // printf("Sentence count: %d\n", scount);
    return scount;
}

int formulate(float l, float w, float s)
{
    float S = (s / w) * 100;
    float L = (l / w) * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;

    int rindex = round(index);

    if (rindex < 2)
    {
        printf("Before Grade 1\n");
    }

    else if (rindex > 15)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %d\n", rindex);
    }

    return 0;
}
