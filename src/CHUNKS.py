
import numpy as np
from typing import List

from src.Utils.DataLoader import DataLoader

from src.Decorator.TimerCMD import Timer

#@Timer.timer()
def image_into_chunks(Image: str, 
                      Depth: int,
                      Height: int, 
                      Width: int) -> List[np.ndarray]:
    """
    Divide a 3D image into chunks and return a list of sub-volumes.

    Parameters:
    -----------
    Image : str
        The file path for loading an array of numbers.
    Depth : int
        Depth dimension of the 3D image.
    Height : int
        Height dimension of the 3D image.
    Width : int
        Width dimension of the 3D image.

    Returns:
    -------
    List[np.ndarray]
        List of sub-volumes.
    """

    # * CHUNKS's size
    CHUNKS = 2;

    # * Initialize a list to store the sub-volumes
    Sub_volumes_CHUNKS = [];

    Image = DataLoader.load_data(Image);

    # * Reshape the array to a 3D array based on the calculated height.
    Image = Image.reshape(Depth, Height, Width);

    # * Calculate the size of each sub-volume
    Sub_depth = (Depth // 2);
    Sub_height = (Height // 2);
    Sub_width = (Width // 2);

    if Depth % 2:
        # * Add a new column of zeros to each slice along the depth dimension
        Image = np.pad(Image, ((0, 1), (0, 0), (0, 0)), mode='constant', constant_values=0);
        print(f"{Depth} is odd");
    
    if Height % 2:
        # * Add a new column of zeros to each slice along the height dimension
        Image = np.pad(Image, ((0, 0), (0, 1), (0, 0)), mode='constant', constant_values=0);
        print(f"{Height} is odd");
    
    if Width % 2:
        # * Add a new column of zeros to each slice along the width dimension
        Image = np.pad(Image, ((0, 0), (0, 0), (0, 1)), mode='constant', constant_values=0);
        print(f"{Width} is odd");
    
    # * Iterate through each sub-volume
    for i in range(CHUNKS):
        for j in range(CHUNKS):
            for k in range(CHUNKS):
                # * Extract the sub-volume from the original image
                Sub_volume = Image[i * Sub_depth:(i + 1) * Sub_depth,
                                    j * Sub_height:(j + 1) * Sub_height,
                                    k * Sub_width:(k + 1) * Sub_width];
                
                Sub_volumes_CHUNKS.append(Sub_volume);

    # * Extract additional chunks
    CHUNK_width = Image[:, :, ((Width // 2) - 1):((Width // 2) + 1)];
    CHUNK_height_1 = Image[:, ((Height // 2) - 1):((Height // 2) + 1), :((Width // 2))];
    CHUNK_height_2 = Image[:, ((Height // 2) - 1):((Height // 2) + 1), ((Width // 2)):Width];
    CHUNK_depth_1 = Image[((Depth // 2) - 1):((Depth // 2) + 1), :((Height // 2)), :((Width // 2))];
    CHUNK_depth_2 = Image[((Depth // 2) - 1):((Depth // 2) + 1), ((Height // 2)):Height, :((Width // 2))];
    CHUNK_depth_3 = Image[((Depth // 2) - 1):((Depth // 2) + 1), :((Height // 2)), ((Width // 2)):Width];
    CHUNK_depth_4 = Image[((Depth // 2) - 1):((Depth // 2) + 1), ((Height // 2)):Height, ((Width // 2)):Width];

    # * Append additional chunks to the list
    Sub_volumes_CHUNKS.extend([CHUNK_width, CHUNK_height_1, CHUNK_height_2, CHUNK_depth_1, CHUNK_depth_2, CHUNK_depth_3, CHUNK_depth_4]);

    return Sub_volumes_CHUNKS