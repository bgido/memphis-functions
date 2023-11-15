## memphis-functions

# This function parses a json file and replaces the severity values with other values according to the following logic -
If the value of the severity = 1, it replaces 1 with low
If the value of severity = 2, it replaces 2 with medium
If the value of the severity = 3, it replaces 3 with high
If the value of the severity = 4, it replaces 4 with critical
If the value of the severity = warning, it replaces warning with low
If the value of severity = minor, it replaces minor with medium
If the value of the severity = major, it replaces major with high
If the value of the severity = critical, it leaves critical as critical
The output is json with the new values of the severity field
