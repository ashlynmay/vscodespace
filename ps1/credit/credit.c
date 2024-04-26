#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

void count(long card);
void checksum(long card);
int result = 0;
int length = 0;

int main()
{
    long card = get_long("Card Number: ");
    void checksum(long card);
    count(card);
}

void count(long card)
{
    for (long i = card; i != 0; i = i / 10)
    {
        length++;
    }

    if (length == 13 || length == 15 || length == 16)
    {
        checksum(card);
    }

    long ss = 1;
    for (long i = length - 2; i != 0; i--)
    {
        card /= 10;
    }
    if (result % 10 == 0)
    {
        if ((card == 40 || card == 41 || card == 42 || card == 43 || card == 44 || card == 45 ||
             card == 46 || card == 47 || card == 48 || card == 49) &&
            (length == 13 || length == 16))
        {
            printf("VISA\n");
        }
        else if ((card == 51 || card == 52 || card == 53 || card == 54 || card == 55) &&
                 length == 16)
        {
            printf("MASTERCARD\n");
        }
        else if ((card == 34 || card == 37) && length == 15)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}

void checksum(long card)
{
    long mod = 10;
    int r1 = 0;
    long card1 = card / 10;
    int r2 = 0;
    int secondr = 0;

    for (int i = length / 2; i > 0; i--)
    {
        r1 = 0;
        r1 = card1 % mod;
        secondr = r1 * 2;
        if (secondr > 9)
        {
            long mod2 = 10;
            for (int j = 2; j > 0; j--)
            {
                r2 = secondr % mod2;
                result += r2;
                secondr /= 10;
            }
            card1 /= 100;
        }
        else
        {
            result += secondr;
            card1 /= 100;
            secondr = 0;
        }
    }

    int ir1 = 0;
    long imod = 10;
    long card2 = card;
    for (int k = 8; k > 0; k--)
    {
        ir1 = 0;
        ir1 = card2 % imod;
        result += ir1;
        card2 /= 100;
    }
    if (result % 10 != 0)
    {
        printf("INVALID\n");
    }
}

❯ ./credit
    Card Number: 371449635398431
    AMEX
❯ ./credit
    Card Number: 4111111111111111
    VISA
❯ ./credit
    Card Number: 4111111111111112
    INVALID