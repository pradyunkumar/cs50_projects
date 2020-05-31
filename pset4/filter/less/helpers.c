#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int newcolor;
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            newcolor = round(((image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0));
            image[i][j].rgbtBlue = newcolor;
            image[i][j].rgbtRed = newcolor;
            image[i][j].rgbtGreen = newcolor;
            newcolor = 0;
        }   
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    double Red;
    double Green;
    double Blue;
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            
            Red = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            Green = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            Blue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            
            if (Red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else 
            {
                image[i][j].rgbtRed = round(Red);
            }
            
            if (Green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else 
            {
                image[i][j].rgbtGreen = round(Green);
            }
            
            if (Blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else 
            {
                image[i][j].rgbtBlue = round(Blue);
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int i = 0, n = width / 2; i < n; i++)
        {
            RGBTRIPLE pixel = image[h][i];
            image[h][i] = image[h][width - i - 1];
            image[h][width - i - 1] = pixel;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE duplic[height][width];
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            duplic[x][y] = image[x][y];
        }
    }
    
    double newred = 0;
    double newblue = 0;
    double newgreen = 0;
    double count = 0;
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int l = i - 1; l <= i + 1; l++) 
            {
                for (int s = j - 1; s <= j + 1; s++)
                {
                    if (l >= 0 && l < height && s >= 0 && s < width)
                    {
                        newred += duplic[l][s].rgbtRed;
                        newgreen += duplic[l][s].rgbtGreen;
                        newblue += duplic[l][s].rgbtBlue;
                        count++;
                    }
                }  
            }
            
            image[i][j].rgbtRed = round(newred / count);
            image[i][j].rgbtGreen = round(newgreen / count);
            image[i][j].rgbtBlue = round(newblue / count);
            
            newred = 0;
            newgreen = 0;
            newblue = 0;
            count = 0;
        }
    }
}
