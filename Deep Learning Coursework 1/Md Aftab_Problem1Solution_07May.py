import numpy as np

def load_mnist_data(file_path):
    data = np.loadtxt(file_path, delimiter=',')

    # The first column contains the labels
    y = data[:, 0].astype(int)

    # The remaining columns contain the image pixel values
    x = data[:, 1:]

    # Normalize pixel values to range [0, 1]
    x = x / 255.0
    return x, y

if __name__ == "__main__":
    file_path = "mnist_train.csv"

    # Load the data
    try:
        x_train, y_train = load_mnist_data(file_path)

        # Print some information about the loaded data
        print(f"Loaded {x_train.shape[0]} images")
        print(f"Image data shape: {x_train.shape}")
        print(f"Labels shape: {y_train.shape}")
        print(f"Sample labels: {y_train[:10]}")
        print(f"Min pixel value: {x_train.min()}")
        print(f"Max pixel value: {x_train.max()}")

    except Exception as e:
        print(f"Error loading data: {e}")