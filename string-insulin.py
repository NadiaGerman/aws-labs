#!/usr/bin/env python3
# coding: utf-8

# Storing the human preproinsulin sequence in a variable called preproInsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Storing the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Merging the results of the smaller insulin groupings into a single variable called insulin:
insulin = bInsulin + aInsulin

# Printing the sequence of human preproinsulin to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain A: " + aInsulin)
print("The sequence of human insulin, chain B: " + bInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Count the number of each amino acid in the insulin sequence
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

# Multiply the count by the weights to get molecular weight
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Calculate error percentage compared to actual molecular weight
molecularWeightInsulinActual = 5807.63
errorPercentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print("Error percentage: " + str(errorPercentage))
