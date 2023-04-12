[Scale Invariant Feature Transform(SIFT)](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf) is an important technique to get important features from any image. The features are invariant to image scale, rotation, and are shown to provide robust matching across a substantial range of affine distortion, change in 3D viewpoint, addition of noise, and change in illumination. 


The SIFT feature detection is available in many advanced packages. But this project will implement only the First part of the Lowe's paper. This is useful if you want to implement SIFT from scratch(using only numpy and PILLOW) and don't want to use the external libraries and I hope this will be good food for curious mind.


***Section-1***

The below steps are used for the implementation of the first part / step-1 of SIFT algorithm which is the detection of the scale space extrema. The implementation of the first step is segregated into some smaller steps which are given below.  

1. Image input and Octave calculation
2. Lowe's Gaussian-Kernel pyramid 
3. Lowe's Gaussian-Blurred Image pyramid 
4. Lowe's DOG pyramid
5. Scale-space extrema in one octave
6. Scale-space extrema in all octave
7. Final function and Dectection of extrema Points


Here we visualize the extrema points on 2 selected images. The main libraries that will be used for this implementation are **PILLOW** and **NUMPY**.

#### 1.2 Lowe's Gaussian-Kernel pyramid

This function gives the standard deviations of gaussian kernels as per the Lowe's paper. The *num_intervals* is similar to the s value represented in the paper. We know at each octave in the input side there is (s+3) no of images including the original image. At the start of the octave we don't do any convolution so the std of gaussian kernel is taken to be 0.

The outer list has length of the total no of octaves and each inner lists have the length of (s+3) which are the kernels' stds. 

#### 1.3 Lowe's Gaussian-Blurred Image pyramid 

Now at first octave level the Image is convolved with all the kernels at first octave. Similarly at the next octave the original image is downsampled by 2 and then convolved with the corresponding kernels at that level. This is done for all the octaves.

#### 1.4 Lowe's DOG pyramid

The below functions is used for the DOG of Images calculation. As we know at each octave the no of DOGs are = (s+2). The Gaussian Kernels are subtracted to get the DOGs at each octave level for all the octaves. The difference is made using [np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html)

#### 1.5 Scale-space extrema in one octave

This funtion find the scale space extrema for each octave present in the image. I have assumed a 3x3x3 kernel of ones which will slice the DOG images and then at each kernel position the mid point is the extrema or not checked. This kernel is moved accross all the DOG images in an octave to get the all extremum points. To take in account of the edge pixels of DOG in scale space I have zero padded the DOG to get if any extremum point is present or not in the DOG.
***Section-2***

Some noise,scale,blur,rotatation is done to see what is happening in the SIFT extrema detection scheme.


***PS: If you use this repo please site. The original paper is attached in the above hyperlink. For sake or readiblility eval.ipynb uploaded on how to use this library with all the intermidiate steps shown.*** 
