Reproducible Science
====================

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


License
-------
This project is licensed under the terms of the [BSD License](/LICENSE)
