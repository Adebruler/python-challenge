import os
import csv

# Add state dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open('employee_data.csv', newline='') as readin:
    # CSV reader specifies delimiter and variable that holds contents
    csvin = csv.reader(readin, delimiter=',')

    # Read the header row first
    csv_header = next(csvin)

    # Open CSV file in which to write reformatted data
    with open('employee_data_update.csv', 'w', newline='') as writeout:
        csvout = csv.writer(writeout, delimiter=',')

        csvout.writerow(['Emp ID', 'First Name', 'Last Name','DOB','SSN','State'])

        # Reformat data read from first document
        for rows in csvin:
            names=rows[1].split()
            date=rows[2].split('-')
            newdate=f'{date[1]}/{date[2]}/{date[0]}'
            ssn=rows[3].split('-')
            newssn=f'***-**-{ssn[2]}'
            state=us_state_abbrev[rows[4]]
            csvout.writerow([rows[0],names[0],names[1],newdate,newssn,state])
