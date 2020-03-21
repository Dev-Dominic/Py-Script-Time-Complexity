#! /usr/bin/env python

import unittest
import os

def get_test_files(): 
    """ Retrieves all the associated test files path """
    path = "test_scripts"
    return [os.path.join(path, test_file) for test_file in os.listdir(path)] 

class TestScriptParsing(unittest.TestCase): 
    """
        Ths unit test module will be used to test 
        the parsing of python scripts.

        test_functions_found: Checks for matching number of functions in a script
        test_basic_ops_count: Checks number of associated basic ops with a given function 
        test_lines_code: Check that the number of lines of code associated with a given function is matches
    """
    unit_tests = get_test_files() # Contains path to test files 

    def test_functions_found(self): 
        pass

    def test_basic_ops_count(self): 
        pass

    def test_lines_code(self): 
        pass

if __name__ == "__main__": 
    print(get_test_files())
    #unittest.main()
