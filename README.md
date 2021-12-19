# CSS503_Team_Supra_Project_2

Low-level vision and high-level vision are commonly thought to be the two subsystems that make up machine vision systems. Low-level vision usually entails processing the incoming image and producing a higher-quality image that is easier to work with machines. Choosing an optimal gray level threshold for differentiating objects from their backgrounds is fundamental in low-level image processing. And the technique is perfectly suited to tackling the situation at hand, and it is complicated enough for release and understanding.

During the threshold implementation we used the following libraries:
```python
import os
import numpy as np
import cv2
import argparse
import ntpath
``` 

When processing photos, choosing an appropriate gray level threshold to identify objects from their backgrounds is critical. In this sense, a variety of approaches have been offered. A histogram should have a deep and steep dip between two peaks, indicating objects and background, so that the threshold can be set at the bottom of this valley. This is the quickest and most understandable way of separating objects from the image background.


Image before processing             |  Image after processing
:-------------------------:|:-------------------------:
![](https://github.com/adilbekishev/CSS503_Team_Supra_Project_2/blob/main/stud.jpg)  |  ![](https://github.com/adilbekishev/CSS503_Team_Supra_Project_2/blob/main/stud_bin.jpg)

