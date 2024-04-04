#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avpxl = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue);
            image[i][j].rgbtRed = round(avpxl / 3.0);
            image[i][j].rgbtGreen = round(avpxl / 3.0);
            image[i][j].rgbtBlue = round(avpxl / 3.0);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sred = round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) +
                             (0.189 * image[i][j].rgbtBlue));
            int sgreen = round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) +
                               (0.168 * image[i][j].rgbtBlue));
            int sblue = round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) +
                              (0.131 * image[i][j].rgbtBlue));

            if (sred > 255)
            {
                sred = 255;
            }

            if (sgreen > 255)
            {
                sgreen = 255;
            }

            if (sblue > 255)
            {
                sblue = 255;
            }

            image[i][j].rgbtRed = sred;
            image[i][j].rgbtGreen = sgreen;
            image[i][j].rgbtBlue = sblue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, rwidth = (width - 1); j < width / 2; j++, rwidth--)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][rwidth];
            image[i][rwidth] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float noa = 0.0;
            int avgr = 0;
            int avgg = 0;
            int avgb = 0;
            for (int k = (i - 1); k <= (i + 1); k++)
            {
                if (k < 0 || k >= height)
                {
                    continue;
                }
                for (int l = (j - 1); l <= (j + 1); l++)
                {
                    if (l < 0 || l >= width)
                    {
                        continue;
                    }
                    else
                    {
                        avgr += image[k][l].rgbtRed;
                        avgg += image[k][l].rgbtGreen;
                        avgb += image[k][l].rgbtBlue;
                        noa++;
                    }
                }
            }
            copy[i][j].rgbtRed = round(avgr / noa);
            copy[i][j].rgbtGreen = round(avgg / noa);
            copy[i][j].rgbtBlue = round(avgb / noa);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
        }
    }

    return;
}
