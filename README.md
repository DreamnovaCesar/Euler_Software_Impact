![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
[![Build Status](https://travis-ci.org/anfederico/clairvoyant.svg?branch=master)](https://travis-ci.org/anfederico/clairvoyant)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<a name="readme-top"></a>

<span style="font-size:1em;"> $${\color{red}{\text{This is version 0.5. Version 1.0 is planned to incorporate this algorithm into a library. However,}}}\newline{\color{red}{\text{for now, you can refer to the description to see how this code can be utilized.}}}$$</span>

# Euler-number-3D-using-Regression-Models

Hey there! I see you're interested in learning about the Euler number. This is a fundamental concept in mathematics that helps us understand the topology of objects in 2D and 3D space.

Let's start with 2D objects. In this case, the Euler number is calculated as the number of connected components (also known as "holes") in a given object minus the number of its boundaries (also known as "genus"). Essentially, it tells us how many holes an object has, and if it's open or closed. The formula for the Euler number in 2D is:

Euler number = Number of connected components - Number of boundaries

It's important to note that the Euler number is always an integer and can be negative, zero, or positive. For example, if an object has one hole and one boundary, the Euler number would be zero. Now, let's move on to 3D objects. The Euler number in this case is calculated in a similar way, but it takes into account not only the number of holes and boundaries, but also the number of handles (or "tunnels"). The formula for the Euler number in 3D is:

Euler number = Number of connected components - Number of handles + Number of boundaries

We present a new library designed to simplify the analysis of Euler characteristics. This program addresses the difficulties involved in generating 3D test objects and the complexities of extracting Octo-Voxel patterns. The library uses a novel method to rapidly generate data, AND extract descriptors by using effective multiprocessing. Furthermore, a method for extracting discrete CHUNKS from an image has been developed, allowing for separate multiprocessing assessment. This method accelerates the process of combination extraction and offers researchers a quick and effective way to look into Euler characteristics in a variety of applications. Our system provides a comprehensive solution for researchers looking for effective ways to create and analyze data, which will advance the discovery of Euler characteristics across a wide range of areas.

## Setup

To set up a virtual environment with TensorFlow using Anaconda (we utilized Python 3.11.7), adhere to the steps outlined below:

Launch the Anaconda Prompt by navigating to the Start menu and searching for "Anaconda Prompt".
Create a new virtual environment named "tfenv" (You can name as you pleased) by executing the following command:

```python
conda create --name tfenv
```

Activate the virtual environment by entering the command:

```python
conda activate tfenv
```

Finally, install the dependencies listed in requirements.txt by running:

```python
conda install requirements.txt
```

By following these steps, you'll successfully create a virtual environment with using Anaconda.

## Code information

- `src`: Contains the main code packages and scripts for execution. This package is divided into:
    - `Data`: Folder for internal storage and some CSV files with patterns extracted previously from different images. 
      Within this folder, there is also a directory named `Images` where the images used for corresponding pattern extraction tests can be obtained.
    - `Utils`: A generic module that includes various functions for configuration and variable saving to be used throughout the code. 
      This same folder contains a file `Utils.py` that houses several of these functions for use across the project.
    - `CHUNKS.py`: A function that divides a 3D image into chunks and returns a list of sub-volumes.
    - `DM.py`: Descriptor Manager (DM) is an abstract class used as a template for creating different classes for the extraction of each descriptor.
        - `OCSC`: Octo-Voxel Contact Surface Chunks (OCSC) - A performance-optimized class for handling Octo-Voxels, leveraging asynchronous approaches and multiprocessing. Utilizes CHUNKS functions for enhanced processing of 3D objects, resulting in substantial speed improvements in the Euler Descriptor Extractor.
        - `OCSMM`: Octo-Voxel Contact Surface Multi Manager (OCSMM) - Asynchronous approaches and multiprocessing are employed in a class created specifically to handle Octo-Voxels, resulting in significant improvements in speed in the Volume Descriptor Extractor.
        - `OCSS`: Octo-Voxel Contact Surface Simplified (OCSS) - A class developed especially for processing Octo-Voxels that uses a simplified method lacking multiprocessing or the CHUNKS technique.
        - `OEC`: Octo-Voxel Euler Chunks (OEC) - A performance-optimized class for handling Octo-Voxels, leveraging asynchronous approaches and multiprocessing. Utilizes CHUNKS functions for enhanced processing of 3D objects, resulting in substantial speed improvements in the Euler Descriptor Extractor.
        - `OEMM`: Octo-Voxel Euler Multi Manager (OEMM) - Asynchronous approaches and multiprocessing are employed in a class created specifically to handle Octo-Voxels, resulting in significant improvements in speed in the Euler Descriptor Extractor.
        - `OES`: Octo-Voxel Euler Simplified (OES) - A class developed especially for processing Octo-Voxels that uses a simplified method lacking multiprocessing or the CHUNKS technique.
        - `OESC`: Octo-Voxel Enclosing Surface Chunks (OESC) - A performance-optimized class for handling Octo-Voxels, leveraging asynchronous approaches and multiprocessing. Utilizes CHUNKS functions for enhanced processing of 3D objects, resulting in substantial speed improvements in the Euler Descriptor Extractor.
        - `OESMM`: Octo-Voxel Enclosing Surface Multi Manager (OESMM) - Asynchronous approaches and multiprocessing are employed in a class created specifically to handle Octo-Voxels, resulting in significant improvements in speed in the Volume Descriptor Extractor.
        - `OESS`: Octo-Voxel Enclosing Surface Simplified (OESS) - A class developed especially for processing Octo-Voxels that uses a simplified method lacking multiprocessing or the CHUNKS technique.
        - `OVC`: Octo-Voxel Volume Chunks (OVC) - A performance-optimized class for handling Octo-Voxels, leveraging asynchronous approaches and multiprocessing. Utilizes CHUNKS functions for enhanced processing of 3D objects, resulting in substantial speed improvements in the Euler Descriptor Extractor.
        - `OVMM`: Octo-Voxel Volume Multi Manager (OVMM) - Asynchronous approaches and multiprocessing are employed in a class created specifically to handle Octo-Voxels, resulting in significant improvements in speed in the Volume Descriptor Extractor.
        - `OVS`: Octo-Voxel Volume System (OVS) - A class developed especially for processing Octo-Voxels that uses a simplified method lacking multiprocessing or the CHUNKS technique.
    - `Generator.py`: An abstract class for generating and saving matrices.
        - `MatrixGenerator.py`: A class for generating and saving matrices.
        - `VoxelGenerator.py`: A class for generating and saving 3D matrices.

- `Main_test_analysis_folders.py` : This function is responsible for utilizing various classes to analyze folders and extract the images within them for shape descriptor analysis. It exclusively deals with 3D objects with resolutions of 4, 8, 16, and 32. Its purpose is to assess the duration of multiprocessing analysis for each image on the testing machine. It's important to note that these specific classes do not employ the CHUNKS method; instead, they analyze each image in a conventional manner, relying on the number of cores allocated or available processing power.

- `Main_test_analysis` : This function employs both the simple method and the CHUNKS method. Here, 14 test images are utilized, which can be found in the `src\Data\Images` folder.

- `Main_test_generator.py` : This function solely generates random objects. You specify the path, the object's resolution, and the desired number of objects.

## Images 

These images depict the 3D objects utilized in the study, offering a visual representation of the image types employed for this experiment.

![Sphere0](/Images/Sphere0_65_65_31_0.png)

![Sphere5](/Images/Sphere5_65_65_31_0.png)

![Squirrel](/Images/Squirrel_128_128_128_0.png)

![Vase](/Images/Vase_69_53_41_0.png)

## Examples

Initially, the algorithm will be utilized to generate 3D objects. This algorithm serves as an exemplar for constructing objects for subsequent utilization. Despite the images being generated at a resolution of 32x32x32, the method incorporates a +2 increment to each measurement. This additional space surrounding the object is imperative to facilitate the enhanced extraction of the octa-voxels. Thus, resulting in objects of dimensions 34x34x34 in this scenario.

```python
from src.VoxelGenerator import VoxelGenerator

def main():

    Voxel_generator = VoxelGenerator(path = r"src\Data\Images_32_3D", 
                                     depth = 32, 
                                     width = 32, 
                                     height = 32, 
                                     num_matrices = 1000);
    
    Voxel_generator.generate_matrices();

if __name__ == '__main__':
    # For Windows support
    main();

```

The ensuing 3D object images exemplify the potential output of a resolution of 34x34x34.

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px;">
    <img src="/Images/Example_32_0_0.png" alt="drawing" width="200"/>
    <img src="/Images/Example_32_1_0.png" alt="drawing" width="200"/>
</div>

Currently, if you're considering the creation of this main function, I highly recommend it, especially for multiprocessing classes.

"src\Data\Images_32_3D" refers to the images for this test; each one is a CSV file. It's important to note that OEMM is specifically designed for directories, and this class employs multiprocessing to extract the Euler descriptor from each image. The degree of parallelism is contingent upon the number of CPU cores accessible. This code is configured to utilize half of the available cores, but you have the option to modify this value. However, exercise caution when making adjustments.

```python
from src.OEMM import OEMM
from src.Utils.Utils import save_to_csv

def main():
    # * Example usage
    Euler_multiprocessing = OEMM(r"src\Data\Images_32_3D");
    Combinations_all, Euler_all, Descriptor = Euler_multiprocessing.get_array(32 + 2, 32 + 2, 32 + 2);
    save_to_csv(r"src\Data", r"src\Data\Images_32_3D", Descriptor, Combinations_all, Euler_all);

if __name__ == '__main__':
    # For Windows support
    main();

```
The difference is small because you only need to change the appropriate class for your the task; everything else remains unchanged. However, it's important to remember that some of these classes depend completely on multiprocessing, which can lead to worse performance. The speed is determined by both the hardware you use and the size of the images.

```python
from src.OES import OES
from src.Utils.Utils import save_to_csv

def main():
    # * Example usage
    Euler_multiprocessing = OES(r"src\Data\Images_32_3D");
    Combinations_all, Euler_all, Descriptor = Euler_multiprocessing.get_array(32 + 2, 32 + 2, 32 + 2);
    save_to_csv(r"src\Data", r"src\Data\Images_32_3D", Descriptor, Combinations_all, Euler_all);

if __name__ == '__main__':
    # For Windows support
    main();

```
For individual images, we recommend using the OEC for extracting the Euler number. The OEC is an algorithm designed for the proposed article, which introduces an innovation called CHUNKS. This algorithm enables us to partition images into chunks, allowing for parallel examination of each and quicker determination of the number of Octo-voxels. Vectorization is employed to accelerate processing, as required by Python. Below is an example of how to use it. If you intend to use a single image, remember that this algorithm relies on CSV files.

Recall that every class listed above has the same Octo-voxel extraction capabilities; the only difference is that the functionality depends on the shape descriptor that is needed.

```python
from src.OEC import OEC
from src.Utils.Utils import save_to_csv

def main():
    # * Example usage
    Euler_multiprocessing = OEC(r"src\Data\Images_32_3D");
    Combinations_all, Euler_all, Descriptor = Euler_multiprocessing.get_array(32 + 2, 32 + 2, 32 + 2);
    save_to_csv(r"src\Data", r"src\Data\Images_32_3D", Descriptor, Combinations_all, Euler_all);

if __name__ == '__main__':
    # For Windows support
    main();

```

The values within the get_array method are the depth, height, and width. In this part, you must enter the exact values of these dimensions so that it can perform a reshape operation. The rationale for adding '+ 2' to each measurement is that the folder has a resolution of 34x34x34, as that was how the data was originally created. If you have an image and know its dimensions, use those dimensions as parameters in the method.

## Co-authors

- Dr. Hermilo Sanchez Cruz

### Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)&nbsp;

### Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

### 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.linkedin.com/in/cesar-eduardo-mu%C3%B1oz-chavez-a00674186/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/CesarEd43166481"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>