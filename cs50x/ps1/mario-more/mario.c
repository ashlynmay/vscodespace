#include <cs50.h>
#include <stdio.h>

void print_row(int length, int spaces);

int main()
{
    // Get height 1-8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height > 8 || height < 1);
    int sub = height - 1;
    for (int i = 0; i < height; i++)
    {
        print_row(i + 1, sub);
        sub--;
    }
}

// Print Rows
void print_row(int length, int spaces)
{
    for (; spaces > 0; spaces--)
    {
        printf(" ");
    }

    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("  ");
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("\n");
}
