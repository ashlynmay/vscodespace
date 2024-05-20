#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int i = 0;
string player[2];
int point[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

void makelower();
void whowon();
void score(string input);
int scored[2];

int main(void)
{

    while (i < 2)
    {
        player[i] = get_string("Player %d: ", i + 1);
        i++;
    }

    makelower();
    i = 0;

    while (i < 2)
    {
        score(player[i]);
        i++;
    }

    whowon();
}

// Convert the characters in players responses to lowercase
void makelower()
{
    int k = 0;
    for (int l = 0; l < i; l++, k++)
    {
        for (int j = 0; j < strlen(player[k]); j++)
        {
            player[k][j] = tolower(player[k][j]);
        }
    }
}

// Calculates players score
void score(string input)
{
    for (int z = 0, len = strlen(input); z < len; z++)
    {
        if (input[z] >= 'a' && input[z] <= 'z')
        {
            scored[i] += point[input[z] - 'a'];
        }
    }
}

// Compares the players scores
void whowon()
{
    if (scored[0] > scored[1])
    {
        printf("Player 1 wins!\n");
    }

    else if (scored[0] < scored[1])
    {
        printf("Player 2 wins!\n");
    }

    else
    {
        printf("Tie!\n");
    }
}
