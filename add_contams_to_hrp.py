#############################
'''
This is a script to add contaminants from cRAP to a Human Reference Proteome from UniProt
This script works with two additional scripts: get_fasta.py and get_cRAP.py. 
''''
#############################
#Import the necessary modules
import os
import sys
import logging
import subprocess

mkdir contams
cd /home/kcoetzer/contams

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
fasta_file_path = fasta_file
with open(fasta_file_path, 'r') as file:
    # Read the existing content of the FASTA file
    fasta_content = file.read()

# Read the cRAP contaminants
crap_file_path = contam_file
with open(crap_file_path, 'r') as file:
    # Read the cRAP FASTA content
    crap_content = file.read()

# Split the cRAP content into individual entries
crap_entries = crap_content.split(">")

# Process and append cRAP contaminants
for entry in crap_entries:
    # Skip empty entries
    if not entry.strip():
        continue

    # Split the entry into header and sequence
    header, sequence = entry.split("\n", 1)
    sequence = sequence.replace("\n", "")

    # Append the cRAP contaminant to the FASTA content
    fasta_content += f">{header}\n{sequence}\n"

# Write the updated content to a new FASTA file
output_file_path = output_file
with open(output_file_path, 'w') as file:
    file.write(fasta_content)

#This block of code checks if the script is being executed as the main module. 
#It initializes the variables extra_file, fasta_file, and output_file to empty strings. 
#It handles command-line argument parsing (not shown in the code) and prompts the user for input to set the values of these variables. 
#Finally, it calls the fasta_add_extras function with the provided arguments.
if __name__ == '__main__':
    contam_file = ''  # Assign the path to the contaminants file
    fasta_file = ''  # Assign the path to the input FASTA file
    output_file = ''  # Assign the path to the output FASTA file

    # Check if database names were passed as command-line arguments
    if len(sys.argv) == 4:
        if os.path.exists(sys.argv[1]):
            contam_file = sys.argv[1]
        else:
            print("Contaminants file not found.")


#####
'''
END
''''
#####
