b=0

if n > 8 reprompt
if n < 1 reprompt


string n = get_string("Height: \n")
loop n times {
b++
s--
printf "#(b)  #(b)"
}

print 2 hashes per line in separate columns & add 1 to both columns per row

n = bottom layer width
topspace = n - 1
space = topspace - 1


   # #
  ## ##
 ### ###
#### ####

int i = 0;
    int z = 0;
    for (; n > 0; n--, --i, --z)
    {
        for(; i == 0; ++i)
        {
        printf("#");
        }

   printf("  ");

        for(; z == 0; ++z)
        {
        printf("#");
        }
    }

    int n = get_int("Height: ");
    int s = n;
    int p = 4;
    for (; n > 0; n--, ++p)
    {
        p -= 4;
        for (; s > p; s--)
        {
            printf(" ");
        }
        printf("#\n");
