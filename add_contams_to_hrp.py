#Import the necessary modules
import os
import sys
import logging
import subprocess

# Run get_fasta.py script
subprocess.run(['python', 'get_fasta.py'])

# Run get_cRAP.py script
subprocess.run(['python', 'get_cRAP.py'])

# Set up logging
#Send output to a log file (log_fasta_contam.txt)
loglevel = 'DEBUG'  # Replace with the desired log level
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(format='%(asctime)s %(message)s', level=numeric_level, filename='log_fasta_contam.txt')
log = logging.getLogger("fasta_contam")
log.info("This is when this event was logged.")
log.warning("Something is not quite right.")
logging.debug('Try again.')
logging.error('Something went wrong.')

# Open the input FASTA file
fasta_file_path = "HRP.fasta"
with open(fasta_file_path, 'r') as file:
# Read the existing content of the FASTA file
    fasta_content = file.read()
print("Opening input FASTA file")
# Read the cRAP contaminants
crap_file_path = "crap.fasta"
with open(crap_file_path, 'r') as file:
    # Read the cRAP FASTA content
    crap_content = file.read()
print("Reading cRAP FASTA file")
# Split the cRAP content into individual entries
#This line splits the crap_content string into individual entries based on the ">" delimiter and stores the result in the crap_entries list.
crap_entries = crap_content.split(">")

#This block iterates through each entry in the crap_entries list. 
#It first checks if the entry is empty or contains only whitespace. 
#If yes, it skips that entry and moves to the next one.
# Process and append cRAP contaminants
for entry in crap_entries:
    # Skip empty entries
    if not entry.strip():
        continue
#For non-empty entries, it splits the entry into a header and sequence using the first occurrence of the newline character (\n). 
#The sequence is then modified to remove any newline characters. 
#The header and modified sequence are concatenated with the existing fasta_content variable.
    # Split the entry into header and sequence
    header, sequence = entry.split("\n", 1)
    sequence = sequence.replace("\n", "")

    # Append the cRAP contaminant to the FASTA content
    fasta_content += f">{header}\n{sequence}\n"

# Write the updated content to a new FASTA file
output_file_path = "hrp_and_contams.fasta"
with open(output_file_path, 'w') as file:
    file.write(fasta_content)
print("New FASTA file with contaminants made")

#This block of code checks if the script is being executed as the main module.
if __name__ == '__main__':
    contam_file = ''  # Assign the path to the contaminants file
    fasta_file = ''  # Assign the path to the input FASTA file
    output_file = ''  # Assign the path to the output FASTA file

