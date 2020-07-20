import os
paths_list=list()
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
    if suffix.isnumeric() or len(suffix)==0 :
        #print('Invalid Suffix')
        return ['Invalid Syntax']
    if os.path.isfile(path):
        if path.endswith(suffix):
            
            #print(path)
            paths_list.append(path)
            return
        return 
    
    
    for item in os.listdir(path):
        new_path = os.path.join(path,item)
        find_files(suffix,new_path)
        
        
    #print(os.listdir('./testdir/subdir1'))
    #print(os.path.isdir('./testdir/subdir1/a.c'))
    return paths_list
def test_func(paths):
    for path in paths:
        print(path)
    
#test 1
print("List all file with extension .c")
paths_list =[]
test_func(find_files('.c','.'))
print('-----------------------------------------------------------------------')
#test 2
print("List all files with extension of .h")
paths_list =[]
test_func(find_files('.h','.'))
print('-----------------------------------------------------------------------')

# TEST 3
paths_list =[]
print("checking with invalid syntax")
test_func(find_files('','.'))
print('-----------------------------------------------------------------------')
