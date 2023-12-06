# %%
import gspread
import pandas as pd
import os

# Write there your directory or it would
# check the /sensitive/ folder.
# WARNING ACHTUNG ВНИМАНИЕ
# Don't let this folder get synced
# or get it into .gitignore
# else it would leak your credentials
# and your user's data.
directory = 'sensitive/'

# Now it'd find json credentials
# and a csv export file
csv_name = ''
files = os.listdir(directory)

for i in files:
    if i[-3:] == str('csv'):
        csv_name = directory+i
        break
print('loaded:', csv_name)

json_name = ''
for i in files:
    if i[-4:] == str('json'):
        json_name = directory+i
        break
print('loaded:', json_name)

# Pull Google Sheet (should be allowed)
# to compare their lenght
gc = gspread.service_account(filename=json_name)
google_sheet = gc.open("VIII Гордеевский фестиваль")
google_df = pd.DataFrame(google_sheet.sheet1.get_all_values())
google_len = len(google_sheet.sheet1.col_values(1))-1

# Set the first row from GS as column names
google_df.columns = google_df.iloc[0]
google_df = google_df[1:]

# Open CSV to compare their lenght
csv_df = pd.read_csv(csv_name)
csv_len = len(csv_df['Entry ID'])

# Fill NaN and sort values to match
# you can customize this value
fill_with = '-'
google_df, csv_df = google_df.fillna(fill_with), csv_df.fillna(fill_with)
csv_df = csv_df.sort_values(by=['Entry ID'], ascending=True)

# Calculate difference between their lenghtes
print('# of strings in GSS: ', google_len)
print('# of strings in CSV: ', csv_len)
difference = csv_len - google_len

# Check if columns list and labels matches
if csv_df.columns.all() == google_df.columns.all():

    # Check if len difference exists
    if difference > 0:
        print("They differ by ", difference, ' strings!')

    # If yes, we push new lines to Google Sheets in a cycle
        current_row = google_len + 1

        for i in range(difference+1):
            taken_row = csv_df.iloc[current_row-2].astype('str')
            diff_range = str('A' + str(current_row) + ':S' + str(current_row))
            if google_sheet.sheet1.cell(current_row,1).value == None:
                google_sheet.sheet1.update(values =
                                        [taken_row.values.tolist()],
                                        range_name = diff_range)
            current_row+=1
        print('Tables are in sync.')
        
    elif difference < 0:
        print('Your CSV has less entries than Google Sheets. Wrong SCV?')
        
    else: print('Tables are in sync. No actions needed.')
    
else: print ('Column labels don\'t match. Wrong tables?')
# End process positively


