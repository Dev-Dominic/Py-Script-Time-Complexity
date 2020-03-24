#! /usr/bin/env python

import unittest
import os


class TestScriptParsing(unittest.TestCase): 
    """
        
    Ths unit test module will be used to test the parsing of python scripts.
        
    test_tmp_file      
    test_time_complex_output

    """
    def get_test_files(): 
        """ Retrieves all the associated test files path """
        path = "test_scripts"
        return [os.path.join(path, test_file) for test_file in os.listdir(path)] 

    def test_tmp_file(self): 
        """ 
        Checks whether tmp output file exists and whether the contents
        match the 
        """
        unit_tests = get_test_files()

    def test_time_complex_output(self): 
        pass

if __name__ == "__main__": 
    print(get_test_files())
    #unittest.main()
