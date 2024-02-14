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

The Euler number in 3D also has some practical applications, such as in computer graphics, where it can be used to detect topological changes in objects or surfaces. In summary, the Euler number is a powerful tool that helps us understand the topology of objects in 2D and 3D space. It's calculated by counting the number of connected components, boundaries, and handles, and it can be negative, zero, or positive.

Artificial Neural Networks (ANNs) are machine learning models that are designed to mimic the structure and function of the human brain. They are particularly well-suited for solving complex problems, such as those involving pattern recognition, data classification, and regression analysis.

In the context of finding the Euler number, ANNs can be used to analyze images or other types of data and identify the underlying topological features, such as the number of connected components, boundaries, and handles. This is because ANNs are able to process large amounts of data, identify patterns, and make predictions based on that data.

For example, an ANN could be trained on a large dataset of 2D or 3D objects, and then used to classify new objects based on their Euler number. The ANN could be trained to recognize patterns in the data that correspond to objects with specific Euler numbers, and then make predictions based on those patterns.

We developed a new method to calculate the Euler number using an Artificial Neural Network (ANN). We found X number of combinations of octo-voxels and added each one to a list. The list, which had a range of 255 elements for each combination, represented the feature set of the data used as input for the ANN. The output was the number of eulers that we calculated. We developed another technique to calculate the Euler number using an artificial neural network from this paper.

## Setup

To create a virtual environment with TensorFlow using Anaconda, follow these steps:

Open the Anaconda Prompt by clicking the Start button and typing "Anaconda Prompt".
Type the following command to create a new virtual environment called "tfenv":

```python
conda create --name tfenv
```

Activate the virtual environment by typing:

```python
conda activate tfenv
```

Finally, install requirements.txt.

```python
conda install requirements.txt
```

## GPU setup

CUDA is a parallel computing platform and programming model developed by NVIDIA for general computing on graphics processing units (GPUs), and cuDNN is a library developed by NVIDIA for deep learning applications. Here are the steps to install both CUDA and cuDNN on your system:

- Check the version of [TensorFlow](https://www.tensorflow.org/install/source#gpu) that you can use.
- You need to install Visual Studio; the documentation explains which version of VS you need. The one we used was [Visual Studio 2019.](https://my.visualstudio.com/Downloads?q=Visual%20Studio%202019)
- Check if your system has an NVIDIA GPU and if it is compatible with CUDA. You can check the list of CUDA-compatible GPUs at the NVIDIA website.
- Download the CUDA Toolkit and cuDNN from the NVIDIA website. You will need to create an NVIDIA developer account to access the downloads.

The following document gives every link used for this process.

```bash
tensorflow GPU.txt
```

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