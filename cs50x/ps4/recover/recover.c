#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
int blocksize = 512;
int fileno = 000;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover card.raw\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file != NULL)
    {
        // Create a buffer for a block of data
        uint8_t buffer[512];
        FILE *jpg = NULL;
        // While there's still data left to read from the memory card
        while (fread(buffer, 1, blocksize, file) == blocksize)
        {
            if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) &&
                ((buffer[3] & 0xf0) == 0xe0))
            {
                if (jpg != NULL)
                {
                    fclose(jpg);
                    fileno++;
                }
                char filename[8];
                sprintf(filename, "%03i.jpg", fileno);
                jpg = fopen(filename, "w");
                if (jpg != NULL)
                {
                    fwrite(buffer, 1, blocksize, jpg);
                }
            }
            else
            {
                if (jpg != NULL)
                {
                    fwrite(buffer, 1, blocksize, jpg);
                }
            }
        }
        if (jpg != NULL)
        {
            fclose(jpg);
        }
    }
    fclose(file);
}
