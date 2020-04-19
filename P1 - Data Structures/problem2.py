import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    paths = []
    # Let us print the files in the directory in which you are running this script
    ls = os.listdir(path)
    for f in ls :
        if os.path.isfile(os.path.join(path, f)) :
            if f.endswith(suffix) :
                paths.append(os.path.join(path, f))
        else:
            paths += find_files(suffix, os.path.join(path, f))
    
    return paths

print(find_files('.c', './testdir'))
# ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']
print(find_files('.c', './testdir/subdir1'))
# ['./testdir/subdir1/a.c']
print(find_files('.c', './testdir/subdir2'))
# []
print(find_files('.c', './testdir/subdir3/subsubdir1'))
# ['./testdir/subdir3/subsubdir1/b.c']