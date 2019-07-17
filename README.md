# imageThresholding

## Types

    Simple Thresholding
    Adaptive Thresholding
    Otsu's Thresholding
   
### Simple Thresholding

    if pixelValue > thresholdValue:
      assign one value (may be white)
    else:
      assign another value (may be black)
      
#### Types

   * cv2.THRESH_BINARY 
   * cv2.THRESH_BINARY_INV
   * cv2.THRESH_TRUNC
   * cv2.THRESH_TOZERO
   * cv2.THRESH_TOZERO_INV

### Adaptive Thresholding

   Calculates the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.
   
   
#### Types

1) Adaptive Method - It decides how thresholding value is calculated.

cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.

cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

2) Block Size - It decides the size of neighbourhood area.

3) C - It is just a constant which is subtracted from the mean or weighted mean calculated.

### Otsu’s Binarization

Finds a threshold value that minimizes weighted within class variation

## MatplotLib

    matplotlib.pyplot.xticks(ticks=None, labels=None, ** kwargs)
    
    ticks --> A list of positions at which ticks should be placed.
    
          --> Passing an empty list will disable xticks.
    
    labels --> A list of explicit labels to place at the given locations.
    
    **kwargs --> Text properties can be used to control the appearance.
