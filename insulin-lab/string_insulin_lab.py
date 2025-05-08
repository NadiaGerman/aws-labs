#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Store the human preproinsulin sequence in a variable
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Merge the smaller sequences into one full insulin variable
insulin = bInsulin + aInsulin

# Print the sequences
print("The sequence of human preproinsulin:")
print(preproInsulin)

print("The sequence of human insulin, chain a:", aInsulin)
print("The sequence of human insulin, chain b:", bInsulin)

# Molecular weight dictionary
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Count amino acids in insulin
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights}

# Compute molecular weight
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights)
print("The rough molecular weight of insulin:", molecularWeightInsulin)

# Compare to actual weight
molecularWeightInsulinActual = 5807.63
errorPercentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print("Error percentage:", errorPercentage)

