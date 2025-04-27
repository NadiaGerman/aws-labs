         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
# Preparing to Analyze Insulin with Python

This project was completed as part of an AWS Cloud9 lab exercise focused on using Python for biological data manipulation.

## Project Overview
The goal of this lab was to retrieve the human preproinsulin sequence, clean it, and split it into functional insulin components for further analysis.

## Files Included

| File Name | Purpose |
|:---|:---|
| `analyze-insulin.py` | Python script to clean and split the insulin sequence |
| `preproinsulin-seq.txt` | Raw insulin sequence (copied from NCBI Protein database) |
| `preproinsulin-seq-clean.txt` | Cleaned insulin sequence (110 amino acids) |
| `lsinsulin-seq-clean.txt` | L chain (first 24 amino acids) |
| `binsulin-seq-clean.txt` | B chain (amino acids 25–54) |
| `cinsulin-seq-clean.txt` | C chain (amino acids 55–89) |
| `ainsulin-seq-clean.txt` | A chain (amino acids 90–110) |

## Lab Steps Completed

- Accessed AWS Cloud9 environment
- Retrieved raw insulin protein sequence from NCBI
- Cleaned the sequence using Python
- Split the cleaned sequence into L, B, C, and A chains
- Verified all file outputs and character counts

## Commands Used

- Linux commands: `pwd`, `ls`, `cat`, `wc -m`
- Python 3 scripting

# String Sequence and Molecular Weight Calculation Lab

This project works with human insulin string sequences and calculates its molecular weight using basic Python features.

## Tasks Completed
- Stored parts of the insulin sequence in string variables
- Printed sequence parts to the console
- Calculated rough molecular weight of insulin based on amino acid composition
- Calculated the error percentage compared to the real molecular weight

## Main File
- `string-insulin.py`: Python script for string manipulations, printing, and molecular weight calculation.


## Author

Nadia  Gilgof-German

---


