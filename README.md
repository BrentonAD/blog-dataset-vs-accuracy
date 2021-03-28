# Training Dataset Size vs Model Accuracy
This repository contains the supporting code for my blog on the affect of training dataset size on model accuracy.
This includes the code to define the ML models, run the experiments, and plot the results.

## Environment Set-up
To download and install the necessary packages I recommend using Anaconda Package manager. Navigate to the root directory of this project and run the below command:

```
conda env create -f environment.yml
```

Once you have created the above environment I recommend installing [nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels) in your base (or preferred) environment for easy access to the environment in jupyter lab. You can install the above package by running

```
conda install -n notebook_env nb_conda_kernels
```

Once your environment has ben set up simply run `jupyter lab` or `jupyter notebook`, open `GeneratePlots.ipynb`, and select the appropriate kernel.

## Contents
This project has the following structure

    .
    ├── data
        ├── input                       # Compressed MNIST data for model training
        └── output                      # JSON outputs of accuracies from experiment runs              
    ├── networks                    # Define Neural Networks to use for experiments
        ├── cnn_network.py
        └── network.py                          
    ├── util
        └── mnist_loader            # Used to load MNIST data for model training                     
    ├── GeneratePlots.ipynb         # Generates plots and runs experiments from blog                    
    ├── environment.yml
    └── README.md

## Acknowledgements
I'd like to extend a huge thank you to *Michael Nielsen* for providing the code in `network.py` and `mnist_loader.py` as well as introducing this problem.

For anyone interested in learning about the fundamentals of Deep Learning and Neural Networks I would highly recommend his book:

[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)