# Py-Script-Time-Complexity v1 (Basic Python Scripts)
Open Source project to analyze the time complexity of python scripts

Version 1 only allows for the analysis of basic python scripts that do not contain looping or recursive function calls. 

## How to use

## Documentation 

To analyze the time-complexity of a given python script it will be broken down into three phases. As follows: 
    1. File Parsing
        - File Analysis(Includes validating python script)
        - Counting of Basic Operations
        - Storage of other related data in tmp file
    2. Time-Complexity Formula 
        - Formulas in terms of input size(n) 
    3. Statistics/Results 
        - Order of Growth
        - Operations Counted
        - Timing statistics given various input sizes 

### Phase Outputs

```
1. File Parsing => (tmp file) 
    - Basic Ops Coutned(dictionary eg. (key: '+', value: 10))
    - Lines of code (int)
    - etc. 

2. File Parsing => Time-Complexity Formula
    - Basic Ops Coutned(dictionary eg. (key: '+', value: 10))

3. (tmp file) => Results 
    - Basic Ops Coutned(dictionary eg. (key: '+', value: 10))
    - Lines of code (int)

4. Formula => Results
    - Time-Complexity Formula String representation
```
