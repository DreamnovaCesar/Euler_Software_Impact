![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
[![Build Status](https://travis-ci.org/anfederico/clairvoyant.svg?branch=master)](https://travis-ci.org/anfederico/clairvoyant)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

<a name="readme-top"></a>

# # Euler-number-3D-using-IA

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