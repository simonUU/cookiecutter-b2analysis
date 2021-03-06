Belle II Analyses Template / Reproducible Science
=================================================

A boilerplate for reproducible and transparent science with close resemblances to the philosophy of [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science): *A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.*

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`    

Usage
-----
To start a new science project:

`cookiecutter gh:simonUU/cookiecutter-b2analysis`

Project Structure
-----------------

```
    
├── AUTHORS.md
├── LICENSE
├── README.md
├── Snakefile               <- Analysis workflow automatization
├── setup_basf2.sh
├── env                     <- Possible conda environments
├── scripts                 <- tools/scripts for data handling
├── data                    <- Data/ NTuples may be remote with symlinks
│   └── example_mc
├── notebooks               <- Analysis Notebooks
├── reports                 <- Belle Note?
│   └── figures
└── reconstruction          <- basf2 steering files
```

Features
--------

 - Analysis scripts

    Pre defined analysis scripts 
    
  - Snakemake automatization
  
    This example can run the analysis script automatically on a set of input data-sets and merges them:
    `snakemake process_data` will run the template analysis script on dummy data.
    
  - Anaconda Envs?
  
  - Belle 2 Note?



License
-------
This project is licensed under the terms of the [BSD License](/LICENSE)
