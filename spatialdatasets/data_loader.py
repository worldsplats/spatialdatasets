# 3ddatasets/data_loader.py
import os
import requests
from pathlib import Path
import zipfile

BASE_URL = "https://example.com/datasets"  # Replace with the actual URL

def download_file(url, destination):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def load(dataset_name):
    data_dir = Path("data")
    dataset_dir = data_dir / dataset_name
    dataset_zip = dataset_dir.with_suffix('.zip')

    # Ensure the data directory exists
    data_dir.mkdir(parents=True, exist_ok=True)

    if not dataset_dir.exists():
        if not dataset_zip.exists():
            # Download dataset
            dataset_url = f"{BASE_URL}/{dataset_name}.zip"
            print(f"Downloading dataset from {dataset_url}...")
            download_file(dataset_url, dataset_zip)

        # Extract dataset
        print(f"Extracting dataset to {dataset_dir}...")
        extract_zip(dataset_zip, data_dir)

    # Return the path to the dataset
    return dataset_dir
