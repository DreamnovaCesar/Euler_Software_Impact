import numpy as np
#import tensorflow as tf

class Config:
    """
    A class that defines data-related constants and configuration options for regression models.

    Attributes
    ----------
    Dataframe_octovoxel_10x10 : str
        File path to the octovoxel 10x10 dataframe.

    Dataframe_octovoxel_Test : str
        File path to the test octovoxel dataframe.

    Folder_data : str
        Path to the data folder.

    Folder_logs : str
        Path to the logs folder.

    Folder_txt : str
        Path to the text folder.

    Test_size : float
        The proportion of the dataset used for testing during training-test splitting.

    Random_state : int
        Seed value for controlling randomness during training-test splitting.

    RF_name : str
        Name of the Random Forest regression model.

    RF_n_estimators : int
        Number of trees in the Random Forest.

    RF_max_depth : int
        Maximum depth of the trees in the Random Forest.

    DT_name : str
        Name of the Decision Tree regression model.

    DT_max_depth : int
        Maximum depth of the Decision Tree.

    Lasso_name : str
        Name of the Lasso regression model.

    Lasso_Alpha : float
        Regularization strength for Lasso regression.

    Lasso_Max_inter : int
        Maximum number of iterations for Lasso regression.

    SVR_name : str
        Name of the Support Vector Regression (SVR) model.

    SVR_C : float
        Regularization parameter for SVR.

    SVR_Kernel : str
        The kernel type used in SVR (e.g., 'linear', 'poly', 'rbf').

    LinearRegression_name : str
        Name of the Linear Regression model.

    MLPRegression_name : str
        Name of the Multi-Layer Perceptron (MLP) Regression model.

    MLP_epochs : int
        Number of training epochs for the MLP model.

    MLP_optimizer : tf.keras.optimizers.Optimizer
        The optimizer used for training the MLP model, such as Adam with a specified learning rate.

    Examples : int
        The number of examples to print.

    Matrix_generator_name : str
        Name of the Matrix Generator.

    Num_matrices : int
        Number of matrices.

    Num_processes : int
        Number of processes.

    Height : int
        Height of the matrices.

    Depth : int
        Depth of the matrices.

    Width : int
        Width of the matrices.

    Octovoxel_size : int
        Size of the octovoxel.

    Byte_binary : str
        Binary number representation.

    _INPUT_3D_ : np.ndarray
        A NumPy array representing the input 3D data.

    _OUTPUT_3D_ : np.ndarray
        A NumPy array representing the output 3D data.
    """

    #=======================================================================================#
    # * Folders used
    Folder_data = r"src\Data";
    Folder_logs = r"src\Data\logs";
    Folder_images = r"src\Data\Images";
    #=======================================================================================#
    # * Folders used voxel generation
    Folder_3D_matrix_4 = r"src\Data\Images_4_3D";
    Folder_3D_matrix_4_1 = r"src\Data\Images_4_1_3D";

    Folder_3D_matrix_8 = r"src\Data\Images_8_3D";
    Folder_3D_matrix_8 = r"src\Data\Images_8_3D";

    Folder_3D_matrix_16 = r"src\Data\Images_16_3D";
    Folder_3D_matrix_16 = r"src\Data\Images_16_3D";

    Folder_3D_matrix_32 = r"src\Data\Images_32_3D";
    Folder_3D_matrix_32 = r"src\Data\Images_32_3D";

    Folder_3D_matrix_128 = r"src\Data\Images_128_3D";
    Folder_3D_matrix_128 = r"src\Data\Images_128_3D";

    Folder_3D_matrix_256 = r"src\Data\Images_128_3D";
    Folder_3D_matrix_256 = r"src\Data\Images_128_3D";

    Matrix_3D_Generator_4_05_05 = [Folder_3D_matrix_4, 4, [0.5, 0.5]]
    Matrix_3D_Generator_4_06_04 = [Folder_3D_matrix_4_1, 4, [0.6, 0.4]]

    Matrix_3D_Generator_8_05_05 = [Folder_3D_matrix_8, 8, [0.5, 0.5]]
    Matrix_3D_Generator_8_06_04 = [Folder_3D_matrix_8, 8, [0.6, 0.4]]

    Matrix_3D_Generator_16_05_05 = [Folder_3D_matrix_16, 16, [0.5, 0.5]]
    Matrix_3D_Generator_16_07_03 = [Folder_3D_matrix_16, 16, [0.7, 0.3]]

    Matrix_3D_Generator_32_05_05 = [Folder_3D_matrix_32, 32, [0.5, 0.5]]
    Matrix_3D_Generator_32_08_02 = [Folder_3D_matrix_32, 32, [0.8, 0.2]]

    Matrix_3D_Generator_128_05_05 = [Folder_3D_matrix_128, 128, [0.5, 0.5]]
    #=======================================================================================#
    # * Folders used matrix generation
    Folder_2D_matrix_4 = r"src\Data\Images_4_2D"
    Folder_2D_matrix_4_1 = r"src\Data\Images_4_1_2D"
    Folder_2D_matrix_4_2 = r"src\Data\Images_4_2_2D"

    Folder_2D_matrix_8 = r"src\Data\Images_8_2D"
    Folder_2D_matrix_16 = r"src\Data\Images_16_2D"
    Folder_2D_matrix_32 = r"src\Data\Images_32_2D"

    Matrix_2D_Generator_4_05_05 = [Folder_2D_matrix_4, 4, [0.5, 0.5]]
    Matrix_2D_Generator_4_06_04 = [Folder_2D_matrix_4_1, 4, [0.6, 0.4]]
    Matrix_2D_Generator_4_03_07 = [Folder_2D_matrix_4_2, 4, [0.3, 0.7]]
    #=======================================================================================#
    # * OH names
    OH_name = "OctovoxelHandler";
    OE_name = "OctovoxelEuler";
    #=======================================================================================#
    # ? MatrixGenerator
    Matrix_generator_name = "MatrixGenerator";
    Num_matrices = 1000;
    Num_processes = 8;
    Height = 32;
    Depth = 32;
    Width = 32;
    #=======================================================================================#
    # * Set the size of octovoxel and calculate the combinations.
    Octovoxel_size = 2;
    #=======================================================================================#
    # * Set the size of octovoxel and calculate the combinations.
    Bitquads_size = 2;
    #=======================================================================================#
    # * Set the size of Octo-Voxel and calculate the combinations.
    Byte_binary = '100000000';
    # * Set the size of Bit-Quads and calculate the combinations.
    Nibble_binary = '10000';
    #=======================================================================================#
    # * Bit-Quads truth table
    _INPUT_2D_ = np.array([     [0, 0, 0, 0],
                                [0, 0, 0, 1],
                                [0, 0, 1, 0],
                                [0, 0, 1, 1],
                                [0, 1, 0, 0],
                                [0, 1, 0, 1],
                                [0, 1, 1, 0],
                                [0, 1, 1, 1],
                                [1, 0, 0, 0],
                                [1, 0, 0, 1],
                                [1, 0, 1, 0],
                                [1, 0, 1, 1],
                                [1, 1, 0, 0],
                                [1, 1, 0, 1],
                                [1, 1, 1, 0],
                                [1, 1, 1, 1]  ], dtype = int);
    #=======================================================================================#
    # * Bit-Quads connectivy 4
    '''Connectivity_4_1 = np.array([   [ 1,  0],
                                    [ 0,  0]    ], dtype = 'int');

    Connectivity_4_2 = np.array([   [ 1,  1],
                                    [ 1,  0]    ], dtype = 'int');

    Connectivity_4_3 = np.array([   [ 1,  0],
                                    [ 0,  1]    ], dtype = 'int');'''

    _OUTPUT_2D_4_ = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, -1, 0], dtype = int);

    #=======================================================================================#
    # * Bit-Quads connectivy 8
    '''Connectivity_8_1 = np.array([   [ 1,  0],
                                    [ 0,  0]    ], dtype = 'int');

    Connectivity_8_2 = np.array([   [ 1,  1],
                                    [ 1,  0]    ], dtype = 'int');
    Connectivity_8_3 = np.array([   [ 0,  1],
                                    [ 1,  0]    ], dtype = 'int');'''

    _OUTPUT_2D_8_ = np.array([0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0], dtype = int);
    #=======================================================================================#
    # * Truth table for training
    _INPUT_3D_ = np.array([ [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1],
                        [0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 0, 0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 1, 1],
                        [0, 0, 0, 1, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 1, 0, 1, 1, 0],
                        [0, 0, 0, 1, 0, 1, 1, 1],
                        [0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1],
                        [0, 0, 0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 1, 1, 0, 1, 1],
                        [0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 1],
                        [0, 0, 0, 1, 1, 1, 1, 0],
                        [0, 0, 0, 1, 1, 1, 1, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 1],
                        [0, 0, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 1, 1, 1],
                        [0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 1, 0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 1, 0, 1, 1],
                        [0, 0, 1, 0, 1, 1, 0, 0],
                        [0, 0, 1, 0, 1, 1, 0, 1],
                        [0, 0, 1, 0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 1, 1, 1, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 1],
                        [0, 0, 1, 1, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 1, 1, 0, 1, 0, 1],
                        [0, 0, 1, 1, 0, 1, 1, 0],
                        [0, 0, 1, 1, 0, 1, 1, 1],
                        [0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 1],
                        [0, 0, 1, 1, 1, 0, 1, 0],
                        [0, 0, 1, 1, 1, 0, 1, 1],
                        [0, 0, 1, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0, 1],
                        [0, 0, 1, 1, 1, 1, 1, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1],
                        [0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 1, 1, 0],
                        [0, 1, 0, 0, 0, 1, 1, 1],
                        [0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 1, 1],
                        [0, 1, 0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 1],
                        [0, 1, 0, 0, 1, 1, 1, 0],
                        [0, 1, 0, 0, 1, 1, 1, 1],
                        [0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 1, 1],
                        [0, 1, 0, 1, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 1, 0],
                        [0, 1, 0, 1, 0, 1, 1, 1],
                        [0, 1, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 1, 1, 0, 0, 1],
                        [0, 1, 0, 1, 1, 0, 1, 0],
                        [0, 1, 0, 1, 1, 0, 1, 1],
                        [0, 1, 0, 1, 1, 1, 0, 0],
                        [0, 1, 0, 1, 1, 1, 0, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0],
                        [0, 1, 0, 1, 1, 1, 1, 1],
                        [0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 0, 1, 0],
                        [0, 1, 1, 0, 0, 0, 1, 1],
                        [0, 1, 1, 0, 0, 1, 0, 0],
                        [0, 1, 1, 0, 0, 1, 0, 1],
                        [0, 1, 1, 0, 0, 1, 1, 0],
                        [0, 1, 1, 0, 0, 1, 1, 1],
                        [0, 1, 1, 0, 1, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 1],
                        [0, 1, 1, 0, 1, 0, 1, 0],
                        [0, 1, 1, 0, 1, 0, 1, 1],
                        [0, 1, 1, 0, 1, 1, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0, 1],
                        [0, 1, 1, 0, 1, 1, 1, 0],
                        [0, 1, 1, 0, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 1, 0],
                        [0, 1, 1, 1, 0, 0, 1, 1],
                        [0, 1, 1, 1, 0, 1, 0, 0],
                        [0, 1, 1, 1, 0, 1, 0, 1],
                        [0, 1, 1, 1, 0, 1, 1, 0],
                        [0, 1, 1, 1, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 1],
                        [0, 1, 1, 1, 1, 0, 1, 0],
                        [0, 1, 1, 1, 1, 0, 1, 1],
                        [0, 1, 1, 1, 1, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0, 1],
                        [0, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 1, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 1, 0],
                        [1, 0, 0, 0, 1, 0, 1, 1],
                        [1, 0, 0, 0, 1, 1, 0, 0],
                        [1, 0, 0, 0, 1, 1, 0, 1],
                        [1, 0, 0, 0, 1, 1, 1, 0],
                        [1, 0, 0, 0, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 1, 1],
                        [1, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 0, 0, 1, 0, 1, 1, 0],
                        [1, 0, 0, 1, 0, 1, 1, 1],
                        [1, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 1],
                        [1, 0, 0, 1, 1, 0, 1, 0],
                        [1, 0, 0, 1, 1, 0, 1, 1],
                        [1, 0, 0, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 1, 1, 0, 1],
                        [1, 0, 0, 1, 1, 1, 1, 0],
                        [1, 0, 0, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 0, 1, 0, 0, 1, 0, 0],
                        [1, 0, 1, 0, 0, 1, 0, 1],
                        [1, 0, 1, 0, 0, 1, 1, 0],
                        [1, 0, 1, 0, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 0, 1, 1],
                        [1, 0, 1, 0, 1, 1, 0, 0],
                        [1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 1, 0, 1, 1, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 1],
                        [1, 0, 1, 1, 0, 0, 0, 0],
                        [1, 0, 1, 1, 0, 0, 0, 1],
                        [1, 0, 1, 1, 0, 0, 1, 0],
                        [1, 0, 1, 1, 0, 0, 1, 1],
                        [1, 0, 1, 1, 0, 1, 0, 0],
                        [1, 0, 1, 1, 0, 1, 0, 1],
                        [1, 0, 1, 1, 0, 1, 1, 0],
                        [1, 0, 1, 1, 0, 1, 1, 1],
                        [1, 0, 1, 1, 1, 0, 0, 0],
                        [1, 0, 1, 1, 1, 0, 0, 1],
                        [1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 1, 1, 1, 0, 1, 1],
                        [1, 0, 1, 1, 1, 1, 0, 0],
                        [1, 0, 1, 1, 1, 1, 0, 1],
                        [1, 0, 1, 1, 1, 1, 1, 0],
                        [1, 0, 1, 1, 1, 1, 1, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 1, 1],
                        [1, 1, 0, 0, 0, 1, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1],
                        [1, 1, 0, 0, 0, 1, 1, 0],
                        [1, 1, 0, 0, 0, 1, 1, 1],
                        [1, 1, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 1, 0, 1, 1],
                        [1, 1, 0, 0, 1, 1, 0, 0],
                        [1, 1, 0, 0, 1, 1, 0, 1],
                        [1, 1, 0, 0, 1, 1, 1, 0],
                        [1, 1, 0, 0, 1, 1, 1, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 1],
                        [1, 1, 0, 1, 0, 0, 1, 0],
                        [1, 1, 0, 1, 0, 0, 1, 1],
                        [1, 1, 0, 1, 0, 1, 0, 0],
                        [1, 1, 0, 1, 0, 1, 0, 1],
                        [1, 1, 0, 1, 0, 1, 1, 0],
                        [1, 1, 0, 1, 0, 1, 1, 1],
                        [1, 1, 0, 1, 1, 0, 0, 0],
                        [1, 1, 0, 1, 1, 0, 0, 1],
                        [1, 1, 0, 1, 1, 0, 1, 0],
                        [1, 1, 0, 1, 1, 0, 1, 1],
                        [1, 1, 0, 1, 1, 1, 0, 0],
                        [1, 1, 0, 1, 1, 1, 0, 1],
                        [1, 1, 0, 1, 1, 1, 1, 0],
                        [1, 1, 0, 1, 1, 1, 1, 1],
                        [1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 0, 0, 1, 0],
                        [1, 1, 1, 0, 0, 0, 1, 1],
                        [1, 1, 1, 0, 0, 1, 0, 0],
                        [1, 1, 1, 0, 0, 1, 0, 1],
                        [1, 1, 1, 0, 0, 1, 1, 0],
                        [1, 1, 1, 0, 0, 1, 1, 1],
                        [1, 1, 1, 0, 1, 0, 0, 0],
                        [1, 1, 1, 0, 1, 0, 0, 1],
                        [1, 1, 1, 0, 1, 0, 1, 0],
                        [1, 1, 1, 0, 1, 0, 1, 1],
                        [1, 1, 1, 0, 1, 1, 0, 0],
                        [1, 1, 1, 0, 1, 1, 0, 1],
                        [1, 1, 1, 0, 1, 1, 1, 0],
                        [1, 1, 1, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 0, 0, 1, 0],
                        [1, 1, 1, 1, 0, 0, 1, 1],
                        [1, 1, 1, 1, 0, 1, 0, 0],
                        [1, 1, 1, 1, 0, 1, 0, 1],
                        [1, 1, 1, 1, 0, 1, 1, 0],
                        [1, 1, 1, 1, 0, 1, 1, 1],
                        [1, 1, 1, 1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1, 0, 0, 1],
                        [1, 1, 1, 1, 1, 0, 1, 0],
                        [1, 1, 1, 1, 1, 0, 1, 1],
                        [1, 1, 1, 1, 1, 1, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1] ], dtype = int);
    #=======================================================================================#
    # * Euler Y
    _OUTPUT_3D_ = np.array([    0,  0,  1,  0,  0,  0,  0,  0,  0,  -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, -2, -1, -2, -1, -1, -1, -1,
                                0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0,
                                0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, -1, 0, -1, 0, 0, 0, 0,
                                0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype = int);
    #=======================================================================================#