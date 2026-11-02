import os
from testif import testif

def ed_read(filename, go_from=0, to=-1): 
    '''Returns the contents of an existing file between the specified
    parameters.'''
    with open(filename) as f:
        file_size = f.seek(0, os.SEEK_END)
        
        if to != -1 and to - go_from > file_size - go_from:
            raise IndexError('Desired location exceeds file length.')
        
        f.seek(go_from)
        
        if to == -1:
            return f.read()
        else:
            return f.read(to - go_from)

def ed_find(filename, search_str):
    '''Records every instance of the specified string in an existing file
    and returns an array of the position of each occurence.'''
    indexes = []
    
    with open(filename) as f:
        top = f.seek(0, os.SEEK_END) - len(search_str)
        
        for i in range(0, top + 1):
            if ed_read(filename, i, i + len(search_str)) == search_str:
                indexes.append(i)
    
    return indexes

def ed_replace(filename, search_str, replace_with, occurence=-1):
    '''Replaces the specific occurence or every occurence of the specified
    string with the new desired string in an existing file.
    Returns the number of replacements made.'''
    found_at = ed_find(filename, search_str)
    present_replace_strings = ed_find(filename, replace_with)
    num_replacements = 0
    
    if found_at:
        with open(filename) as f:
            file_str = f.read()
            if occurence == -1:
                file_str = file_str.replace(search_str, replace_with)
                # num_replacements = len(found_at)
                # find true num replacements
                # doesn't give accurate number
            elif occurence >= 0 and occurence <= len(found_at):
                prefix = file_str[:found_at[occurence]]
                suffix = file_str[found_at[occurence]:]
                
                suffix = suffix.replace(search_str, replace_with, 1)
                file_str = prefix + suffix
                # num_replacements = 1
        
        with open(filename, 'w') as f:
            f.write(file_str)
    
    num_replacements = (len(ed_find(filename, replace_with))
                        - len(present_replace_strings)) 
    
    return num_replacements
                    
def ed_append(filename, string):
    '''Writes the specified string to a file.'''
    with open(filename, 'a') as f:
        f.write(string)
    
    return len(string)

def test_ed_replace(filename, search_str, replace_with, occurence):
    found_count = len(ed_find(filename, search_str))
    replace_count = ed_replace(filename, search_str, replace_with, occurence)
    new_found = len(ed_find(filename, search_str))
    
    return testif(found_count - replace_count == new_found, 'ed_replace',
                  'ed_replace is functional', 'ed_replaced failed')

def test_ed_find(filename, search_str):
    with open(filename) as f:
        file_str = f.read()
        search_count = file_str.count(search_str)
        
        return testif(len(ed_find(filename, search_str)) == search_count,
                      'ed_find', 'ed_find is functional', 'ed_find failed')

def main():
    fn = 'fool.txt'
    
    try:
        with open(fn):
            pass
    except FileNotFoundError:
        ed_append('madeafileforyou.txt',
                  'applepicklebananaorangepicklecoffeecream')
        fn = 'madeafileforyou.txt'
    
    print(ed_read(fn, 5, 14))
    print(ed_find(fn, 'coffee'))
    print(ed_replace(fn, 'pickle', 'jazz', 1))
    print(ed_append(fn, 'juicebox'))
    
    
    # test_ed_replace(fn, 'apple', 'orange', -1)
    # test_ed_find(fn, 'pickle')

if __name__ == '__main__':
    main()