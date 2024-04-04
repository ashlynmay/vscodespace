#include <cs50.h>
#include <stdio.h>

int main()
{
    string s = get_string("What should I call you? ");
    printf("hello, %s\n", s);
}
