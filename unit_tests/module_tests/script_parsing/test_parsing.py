#! /usr/bin/env python

# TODO import script_parsing module
# TODO decide whether the script parsing module should handle the creation of tmpDir  
import unittest
import os


class TestScriptParsing(unittest.TestCase): 
    """Test Script Parsing module
    
        GLOBALS: path 
        
        test_tmp_file      
        test_time_complex_output

    """
    test_script_path = "test_scripts"

    def get_test_files(): 
        """Retrieves all the associated test files path 
            
            Args: None
            
            Return: 
                result: test_cases file paths
        """
        result = [os.path.join(path, test_file) for test_file in os.listdir(path)] 

        return result

    def setUP(self): 
        """Execution parsing script to get outputs

            Args: self

            Return: None

        """
        unit_tests = get_test_files()
        self.tmp_files = []
        self.testcase_results = []

        """ Testcases tmp files """ 
        for _file in unit_tests:
            fileTemp = 'tmp_' + _file
            filepath = os.path.join(tmpdirPath, fileTemp)
            self.tmp_files.append(filepath)

            """ Running script parsing module """
            self.testcase_results.append(script_parsing(_file))

    def tearDown(self): 
        """Deletion of tmp files and results

            Args: self

            Return: None

        """
        del self.tmp_files

        """ Clean up of temporary files """ 
        for tmpFile in self.tmp_file:
            try; 
                os.remove(tmpfile)
            except OSError as e:
                print("File Error occured!")

        os.rmdir()
        
    def test_tmp_file(self): 
        """Verifies content of tmp file    

            Args: self

            Return: 
                None
        """
        tmpdirPath = os.path.join(test_script_path, tmpdir)
        os.mkdir(tmpdirPath) # Creates test_scripts tmp_file directory


    def test_time_complex_output(self): 
        """Verifies that proper count of basic ops 

            Args: self

            Return: 
                None 
        """
        pass

if __name__ == "__main__": 
    print(get_test_files())
    #unittest.main()
