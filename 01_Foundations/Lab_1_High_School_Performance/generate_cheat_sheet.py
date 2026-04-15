import csv
import os

# Define the path for the output CSV file
output_file = r'a:\Data Analytics 2_0\Done Labs\Excel_Concepts_Cheat_Sheet.csv'

# Define the headers for the CSV
headers = [
    'Lab Requirement',
    'Excel Concept / Tool',
    'Formula Syntax',
    'Our Example (What we built)',
    'Plain English Explanation'
]

# Define the rows of data based on our learning sessions
data = [
    [
        'Total Number of courses',
        'UNIQUE & COUNTA',
        '=COUNTA(UNIQUE(where_to_look))',
        "=COUNTA(UNIQUE('Original'!A2:A4921))",
        'UNIQUE strips out all duplicates to give us a clean list. COUNTA then counts how many items are in that clean list. Like counting unique programs at the university gate.'
    ],
    [
        'Number of Students enrolled',
        'UNIQUE & COUNTA',
        '=COUNTA(UNIQUE(where_to_look_for_IDs))',
        "=COUNTA(UNIQUE('Original'!C2:C4921))",
        'Same logic as above, but applied to the Student ID column. We always use IDs instead of Names to count people accurately.'
    ],
    [
        'Getting Student Names from IDs',
        'XLOOKUP',
        '=XLOOKUP(what_to_find, where_to_find_it, what_to_return)',
        "=XLOOKUP(D2, 'Original'!C:C, 'Original'!B:B)",
        'Like going to a filing cabinet. You grab the ID (D2), walk to the cabinet (Original C Column), find the match, and pull out the attached name (Original B Column).'
    ],
    [
        'Number of Same Students enrolled in different Courses',
        'COUNTIF',
        '=COUNTIF(where_to_look, what_to_look_for)',
        "=COUNTIF('Original'!C:C, D2)",
        'A tally counter. Excel looks at the whole raw data column of IDs and simply counts how many times the specific ID in cell D2 appears. This tells us how many courses they are in.'
    ],
    [
        'Filtering for >1 Course',
        'COUNTIF (with condition)',
        'COUNTIF(where_to_look, "condition")',
        '=COUNTIF(E2:E116, ">1")',
        'Still a tally counter, but now it checks a math rule. It looks at our calculated course counts and only tallies the ones physically larger than 1.'
    ],
    [
        'The Average score of Each Student',
        'AVERAGEIF',
        '=AVERAGEIF(where_to_check, what_to_look_for, what_to_average)',
        "=AVERAGEIF('Original'!C:C, D2, 'Original'!L:L)",
        'Excel hunts down every row that belongs to the specific student ID (D2), grabs their scores from the L column, and mathematically averages just those scores.'
    ],
    [
        'Fixing #DIV/0! Errors from Dragging',
        'Absolute References ($) OR Whole Columns',
        'Use Column:Column (e.g. C:C) instead of C2:C100',
        '=AVERAGEIF(Original!C:C, ...)',
        'When you drag formulas down, Excel slides the search area down too. Using the whole column (C:C) "padlocks" the search area so it never slips into blank cells.'
    ],
    [
        'Names of 5 Highest ranking students in Each Course',
        'Pivot Tables (The Magic Whiteboard)',
        'Insert > PivotTable',
        'Rows: Course, then Student. Values: Average of Result. Filter: Top 5',
        'Reorganizes massive flat data. Drag course and names to Rows to list them. Drag score to Values and change to Average. Use "Top 10" filter changed to Top 5.'
    ],
    [
        'Pivot Table Messy Layout',
        'Tabular Form',
        'Design Tab > Report Layout > Show in Tabular Form',
        'N/A',
        'Fixes the default "Compact" view that crushes things into one column. Splits courses and students beautifully into their own separate columns.'
    ]
]

# Write the data to the CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Success! The CSV file has been generated at: {output_file}")
