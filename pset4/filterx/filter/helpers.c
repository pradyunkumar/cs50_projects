#include "helpers.h"
#include "math.h"

//convert to grayscale
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
// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE duplic[height][width];
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            duplic[x][y] = image[x][y];
        }
    }
    
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    
    double Gxred = 0.0;
    double Gxblue = 0.0;
    double Gxgreen = 0.0;
    double Gyred = 0.0;
    double Gyblue = 0.0;
    double Gygreen = 0.0;
    int G1 = 0;
    int G2 = 0;
    
    double newred;
    double newblue;
    double newgreen;
    
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int l = i - 1; l <= i + 1; l++) 
            {
                for (int s = j - 1; s <= j + 1; s++)
                {
                    G1 = l - i + 1;
                    G2 = s - j + 1;
                    
                    if (l >= 0 && l < height && s >= 0 && s < width)
                    {
                        Gxred += duplic[l][s].rgbtRed * Gx[G1][G2];
                        Gxgreen += duplic[l][s].rgbtGreen * Gx[G1][G2];
                        Gxblue += duplic[l][s].rgbtBlue * Gx[G1][G2];
                        Gyred += duplic[l][s].rgbtRed * Gy[G1][G2];
                        Gygreen += duplic[l][s].rgbtGreen * Gy[G1][G2];
                        Gyblue += duplic[l][s].rgbtBlue * Gy[G1][G2];
                    }
                }  
            }
            
            newred = sqrt(Gxred * Gxred + Gyred * Gyred);
            newblue = sqrt(Gxblue * Gxblue + Gyblue * Gyblue);
            newgreen = sqrt(Gxgreen * Gxgreen + Gygreen * Gygreen);
            
            if (newred > 255)
            {
                newred = 255;
            }
            
            if (newgreen > 255)
            {
                newgreen = 255;
            }
            
            if (newblue > 255)
            {
                newblue = 255;
            }
            
            image[i][j].rgbtRed = round(newred);
            image[i][j].rgbtGreen = round(newgreen);
            image[i][j].rgbtBlue = round(newblue);
            
            Gxred = 0.0;
            Gxblue = 0.0;
            Gxgreen = 0.0;
            Gyred = 0.0;
            Gyblue = 0.0;
            Gygreen = 0.0;
        }
    }
}

