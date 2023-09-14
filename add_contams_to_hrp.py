# This is a python script to add common contaminants from the cRAP database to the Human Reference Proteome from UniProt. This is an example of a protein database that can be used as input for all proteomics search engines. The output file is in FASTA format.
# Load modules that will be used
import os
import requests
import logging
from Bio import SeqIO

# Configure logging with a basic configuration (https://docs.python.org/3/howto/logging-cookbook.html)
# Logging messages which are less severe than level will be ignored
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a console handler and set its log level to INFO
# StreamHandler sends logging output to streams such as sys.stdout, sys.stderr, or any file-like object
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the console handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the root logger that is created
logging.getLogger('').addHandler(console_handler)

# Defines the function. Give the function a specific name. Specify the files that will be used in the command.
def download_file(url, output_path):
    # Sends an HTTP get request to the provided URL using the requests library. The response from the server is stored in the response variable
    response = requests.get(url)
    # Checks if the HTTP response status code is 200, which indicates a successful request. If the condition is true, it means the file was successfully retrieved from the server.
    if response.status_code == 200:
        # Opens the output_path file in write mode ('w') using a context manager.
        with open(output_path, 'w') as file:
            # Writes the content of the response (the downloaded file) to the opened file
            file.write(response.text)
            # Print log message if successfully saved to output_path
        logging.info(f"File saved as '{output_path}'")
    else:
        # Prints an error message with status code
        logging.error("An error occurred while retrieving the file: %d", response.status_code)

def concatenate_fasta_files(fasta_file_path, crap_file_path, output_file_path):
    # Read sequences from the first input file
    sequences1 = SeqIO.parse(fasta_file_path, "fasta")

    # Read sequences from the second input file
    sequences2 = SeqIO.parse(crap_file_path, "fasta")

    # Concatenate the sequences
    concatenated_sequences = list(sequences1) + list(sequences2)

    SeqIO.write(concatenated_sequences, output_file_path, "fasta")

    logging.info(f"Concatenated sequences saved to {output_file_path}")

# Specify URLs and file names to be used
fasta_url = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28proteome%3AUP000005640%29%29'
crap_url = 'http://ftp.thegpm.org/fasta/cRAP/crap.fasta'
fasta_file_path = "HRP.fasta"
crap_file_path = "crap.fasta"
output_file_path = "HRP_contams.fasta"

# Download FASTA file
# Runs the download file command that was described above
logging.info("Downloading FASTA file...")
download_file(fasta_url, fasta_file_path)

# Download contaminant file
# Runs the download file command that was described above
logging.info("Downloading contaminant file...")
download_file(crap_url, crap_file_path)

# Concatenate fasta files
# Runs the concatenate command described above
logging.info("Concatenating FASTA files...")
concatenate_fasta_files(fasta_file_path, crap_file_path, output_file_path)

# Gives a final log output if the script was executed completely
logging.info("Script execution completed.")
