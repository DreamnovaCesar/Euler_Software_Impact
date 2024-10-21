# * Use Python 3.11.7 as the base image
FROM python:3.12.3

# * Set the working directory in the container
WORKDIR /app

# * Copy the current directory contents into the container at /app
COPY . /app

#The --no-cache-dir option is a command-line argument 
#that you can pass to pip (Python's package installer) when installing packages. 
#It tells pip not to use or create a cache directory for storing downloaded package 
#distributions and metadata.

# * Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# * Specify the command to run your application
CMD ["python", "-m", "Main_test_analysis"]