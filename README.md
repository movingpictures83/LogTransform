# LogTransform
# Language: Python
# Input: CSV (data to be transformed)
# Output: CSV (log-transformed data)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin that takes a CSV file of data values and produces another CSV file
with these values log-transformed.

Note that zero values in the input CSV file will be imputed with the smallest
floating point value available in Python before the log is computed.
