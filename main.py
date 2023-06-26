from pathlib import Path
#from fill_numbers import fill_numbers
from name_gen import name_gen
from from_two_files import from_two_files
from make_files import make_files
from new_make_files import new_make_file
from group_rename import group_rename

if __name__ == '__main__':
   

    make_files('bin', 'dir', count=3 )

    
    group_rename('bin', 'zip', "new_name")