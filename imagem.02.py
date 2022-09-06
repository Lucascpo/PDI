# -*- coding: utf-8 -*-
"""imagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JoF9ASfzjoQWWUX_I_-jSERwIBximLa8
"""

!pip install gdal
!pip install rasterio
!pip install spectral

"""**TIFFFILE**"""

import tifffile as tiff
import matplotlib.pyplot as plt
import numpy as np

img = tiff.imread('/content/Imagens/L71221071_07120010720_DN.tif')

img.shape

plt.imshow(img[:,:,3], cmap= 'Greys_r')

from spectral import imshow

imshow (img, bands=(2,1,0))

"""**GDAL**"""

from osgeo import gdal

img2= gdal.Open ("/content/Imagens/L71221071_07120010720_DN.tif")

print (img2)

img3=img2.ReadAsArray()

img3=img3.swapaxes (0,2)

img3.shape

imshow(img3[:,:,3])

imshow(img3, (2,3,1))

b1=img2.GetRasterBand(1).ReadAsArray()
b2=img2.GetRasterBand(2).ReadAsArray()
b3=img2.GetRasterBand(3).ReadAsArray()

stack=np.dstack([b1,b2,b3])

stack.shape

imshow(stack,(2,1,0))

"""**RASTERIO**"""

import rasterio

rst=rasterio.open('/content/Imagens/L71221071_07120010720_DN.tif')

from rasterio. plot import show

show(rst,cmap='Greys_r')

b1= rst.read (1)
b2= rst.read (2)
b3= rst.read (3)

stack = np.dstack([b1,b2,b3])

imshow (stack, (2,1,0))