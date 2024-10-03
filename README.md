# IllumioTechAssess
Jasmine Liu's submission for Illumio's Technical Assessment

### How to Run:
1. Download the files into one folder.
2. On the terminal, navigate to the folder the files are located on.
3. On the terminal, run `python .\main.py`. If `output.txt` already exists in the folder, the file will be overriden with new values. If the file does not exist, the file will be created. This file contains the expected solution.
4. To test other cases, modify `input.txt`, which contains the flow logs, and `lookup.csv`, which contains the lookup table.

### Assumptions:
1. All of the inputs follow the format given to me in the assignment.
  a. The flow logs are default logs, version 2 only.
  b. The lookup table follows .csv format.
  c. The output is one output file with both the tag counts and port/protocol counts.
2. The only value that I am extracting from the flow logs is the dstport and using that to find both the protocol and tag from the lookup table.
3. In the case that a flow log does not have an associated protocol because the `dstport` does not exist in the lookup table, the protocol listed in the `port/protocol` combination counts is `None`.
