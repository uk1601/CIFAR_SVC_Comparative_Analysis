import os
import tarfile
import urllib.request

def download_and_extract_cifar10(data_dir):
    """
    Downloads and extracts the CIFAR-10 dataset.

    Args:
    data_dir (str): Directory where the dataset should be downloaded and extracted.
    """
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    url = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    filename = os.path.join(data_dir, 'cifar-10-python.tar.gz')
    
    # Download the dataset
    print("Downloading CIFAR-10 dataset...")
    urllib.request.urlretrieve(url, filename)
    print("Download complete.")
    
    # Extract the dataset
    print("Extracting CIFAR-10 dataset...")
    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall(path=data_dir)
    print("Extraction complete.")
    
    # Clean up the tar file
    os.remove(filename)
    print("CIFAR-10 dataset downloaded and extracted successfully.")

# Specify the directory where you want to download and extract the CIFAR-10 dataset
data_dir = './data'
download_and_extract_cifar10(data_dir)

