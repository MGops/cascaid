import time
import os

# Store the prescribing cascades
cascades = {
    'amlodipine': ('furosemide', 'Oedema'),
    'nifedipine': ('furosemide', 'Oedema'),
    'diuretic': ('solifenacin', 'Incontinence'),
    'antipsychotic': ('antiparkinsonian medication', 'EPSEs'),
    'diazepam': ('donepezil', 'cognitive impairment'),
    'lorazepam': ('donepezil', 'cognitive impairment'),
    'diazepam': ('memantine', 'cognitive impairment'),
    'lorazepam': ('memantine', 'cognitive impairment'),
    'sertraline': ('zopiclone', 'insomnia'),
    'fluoxetine': ('zopiclone', 'insomnia'),
    'citalopram': ('zopiclone', 'insomnia'),
    'escitalopram': ('zopiclone', 'insomnia'),
    'venlafaxine': ('zopiclone', 'insomnia'),
    'duloxetine': ('zopiclone', 'insomnia'),
    'nsaid': ('amlodipine', 'hypertension'),
    'nsaid': ('ramipril', 'hypertension'),
    'nsaid': ('lisinopril', 'hypertension'),
    'solifenacin': ('donepezil', 'confusion/ cognitive impairment'),
    'solifenacin': ('memantine', 'confusion/ cognitive impairment'),
    'doxazosin': ('prochlorperazine', 'orthostatic hypotension/ dizziness'),
    'donepezil': ('solifenacin', 'urinary incontinence'),
    'solifenacin': ('omeprazole', 'gastric reflux'),
    'solifenacin': ('movicol', 'constipation'),
    'solifenacin': ('senna', 'constipation'),
    'solifenacin': ('lactulose', 'constipation'),
    'solifenacin': ('docusate', 'constipation'),
    'solifenacin': ('fybogel', 'constipation')
}

print("PRESCRIBING CASCADE CHECKER")
print("Add medications to check for prescribing cascades.\n")


medications = []

#Print subroutine to list the medication that has been entered.
def print_meds():
    os.system("clear")
    print("\nMedication list:")
    print()
    counter = 1
    for med in medications:
        print(f"{counter}: {med}")
        counter += 1
    time.sleep(3)
    os.system("clear")

# Program menu
while True:
    print("What would you like to do?")
    print("Enter the appropriate number from the menu and press Enter.\n")
    menu = input("1. Input medication\n2. List medication\n3. Find cascades\n4. Exit\n\n>")
    if menu == "1":
        new_med = input("Medication: ")
        medications.append(new_med)
    elif menu == "2":
        print_meds()
    elif menu == "3":
        if not medications:
            print("You have not entered any medications")
        else:
            break
    elif menu == "4":
        exit()
    else:
        print("That's not a valid option! ")
    time.sleep(1)
    os.system("clear")
    

# Check for possible prescribing cascades
print("\nChecking for possible prescribing cascades...\n")
time.sleep(2)

found_cascades = []

for med in medications:
    if med in cascades:
        implicated_med, side_effect = cascades[med]
        if implicated_med in medications:
            found_cascades.append((med, implicated_med, side_effect))

# Output possible prescribing cascades
if found_cascades:
    print("Potential ongoing prescribing cascades detected:")
    for cascade in found_cascades:
        print(f"- {cascade[0].upper()} could cause {cascade[2]}, which may have led to {cascade[1].upper()} being prescribed.")
else:
    print("No prescribing cascades detected.")

#To do:
# Add a menu item to remove a medication from the list
# Add more cascades or interactions
# Give an error message if user selects option 3 without having entered any medication
# Find a way to store the info on cascades for individual patients and retrieve