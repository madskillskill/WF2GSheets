# WF2GSheets
Push WeForms plugin's export updates to Google Sheets (WordPress + Python3 + Google APIs)

# You'd need:

1. A WordPress site, admin dashboard access;
2. A free or paid WeForms plugin (to collect application forms, feedback and stuff);
3. A working credentials created with Google, it's plugins: https://console.cloud.google.com/apis/credentials

*I used that article to help myself through the last one: https://www.makeuseof.com/tag/read-write-google-sheets-python/*

# Working with a script

4. After creating a form and giving it some mock replies (see mosk-csv.csv as a sample) you can put it into **/sensitive/** directory to test the push capability. This folder is excluded by .gitignore for a reason. You are meant to save sensitive data here.
5. Launch the script. I created some failsafes, so it'd abort the operation when tables obviously don't match, GSheets has more rows etc.

The output with a mock-csv and an empty sheet would be as follows:

```python
loaded: sensitive/mock-csv.csv
loaded: sensitive/gordeevtable-999418dadd82.json
# of strings in GSS:  0
# of strings in CSV:  5
They differ by  5  strings!
C:\Users\madskillkills\AppData\Local\Temp\ipykernel_17284\3083852811.py:72: DeprecationWarning: [Deprecated][in version 6.0.0]: Method signature's arguments 'range_name' and 'values' will change their order. We recommend using named arguments for minimal impact. In addition, the argument 'values' will be mandatory of type: 'List[List]'. (ex) Worksheet.update(values = [[]], range_name=) 
  google_sheet.sheet1.update(values =
Tables are in sync.
```