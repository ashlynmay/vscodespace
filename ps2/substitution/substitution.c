#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string ptext;
char ctext[27];
char ukey[27];
char lkey[27];

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        for (int j = 0; j < 26; j++)
        {
            if (!isalpha(argv[1][j]))
            {
                printf("Key must contain 26 characters.\n");
                return 1;
            }
        }

        int repeated = 0;
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            for (int j = i + 1; j < strlen(argv[1]); j++)
            {
                if (argv[1][i] == argv[1][j])
                {
                    repeated = 1;
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
            }
        }
        if (strlen(argv[1]) == 26)
        {
            ptext = get_string("plaintext: ");
            for (int n = 0; n <= strlen(argv[1]); n++)
            {
                ukey[n] = toupper(argv[1][n]);
                lkey[n] = tolower(argv[1][n]);
            }
        }
        else
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }

    else
    {
        printf("Usage: ./substition key\n");
        return 1;
    }

    for (int i = 0; i < strlen(ptext); i++)
    {
        if (isalpha(ptext[i]))
        {
            if (isupper(ptext[i]))
            {
                ctext[i] = ukey[ptext[i] - 'A'];
            }
            else
            {
                ctext[i] = lkey[ptext[i] - 'a'];
            }
        }
        else
        {
            ctext[i] = ptext[i];
        }
    }
    printf("ciphertext: %s\n", ctext);
}

❯ ./substitution
    Usage: ./substition key
❯ ./substitution NQXPOMAFTRHLZGECYJIUWSKD
    Key must contain 26 characters.
❯ ./substitution NQXPOMAFTRHLZGECYJIUWSKDVB
    plaintext: hello, world
    ciphertext: folle, kejlp