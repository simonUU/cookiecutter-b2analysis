# Files to index hack for snakemake
#
# Author:  Simon (simon.wehle@desy.de)
#
#
import glob

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def cache_glob_data(loc, file_path, fmax=1):
    """ Since glob takes quite some time, we store the result in a yml file """
    import os
    import yaml
    if file_path is not None and os.path.isfile(file_path):
        with open(file_path) as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    else:
        print("Performing glob ")
        if isinstance(loc, list):
                runs = glob.glob(loc[0])
                li = []
                for r in runs:
                    li+= list(chunks(glob.glob(r + loc[1]), fmax))
        else:
            li = list(chunks(glob.glob(loc), fmax))
        if file_path is not None:
            with open(file_path, 'w') as file:
                yaml.dump(li, file)
        return li

# Expand the globs and save the file lists

class GlobFilesToIndex:
    FILES = {}
    DATASETS = None
    glob_storeage = None

    def __init__(self, data_sets, glob_storage=None):
        self.DATASETS = data_sets
        self.FILES = {}
        for c in self.DATASETS:
            d = self.DATASETS[c]
            if isinstance(d,list):
                nmax = d[1]
                d = d[0]
            else:
                nmax=1
            glob_file_name = f'{glob_storage}{c}_{nmax}.yml' if glob_storage is not None else None
            f = cache_glob_data(d, glob_file_name, nmax)
            self.FILES[c] = f

    def get_files_by_index(self, cat, i):
        assert i < len(self.FILES[cat])
        r = self.FILES[cat][i]
        if isinstance(r, str):
            return [r]
        return r

    def range_nfiles(self, cat):
        return range(len(self.FILES[cat]))