# IllumioTechAssess
Jasmine Liu's submission for Illumio's Technical Assessment. Notes on how the solution works are left in `main.py`.

### How to Run:
1. Download the files into one folder.
2. On the terminal, navigate to the folder the files are located on.
3. On the terminal, run `python .\main.py`. If `output.txt` already exists in the folder, the file will be overriden with new values. If the file does not exist, the file will be created. This file contains the expected solution.
4. To test other cases, modify `input.txt`, which contains the flow logs, and `lookup.csv`, which contains the lookup table.

### Cases Checked:
- Provided sample logs
- Empty logs
- 1 line logs
- Duplicate logs
- 1 entry lookup table
- Empty lookup table
- Uneven capitalization

### Assumptions:
1. All of the inputs follow the format given to me in the assignment.
- The flow logs are default logs, version 2 only.
- The lookup table follows .csv format.
- The output is one output file with both the tag counts and port/protocol counts.
3. The only value that I am extracting from the flow logs is the dstport and using that to find both the protocol and tag from the lookup table.
4. In the case that a flow log does not have an associated protocol because the `dstport` does not exist in the lookup table, the protocol listed in the `port/protocol` combination counts is `None`.
