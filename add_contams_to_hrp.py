#load modules that will be used
import os
import requests


#Defines the function
def download_file(url, output_path):
	#Sends an HTTP GET request to the provided url using the requests library. The response from the server is stored in the response variable
    response = requests.get(url)
    #Checks if the HTTP response status code is 200, which indicates a successful request. If the condition is true, it means the file was successfully retrieved from the server.
    if response.status_code == 200:
    	#Opens the output_path file in write mode ('w') using a context manager
        with open(output_path, 'w') as file:
        	#Writes the content of the response (the downloaded file) to the opened file
            file.write(response.text)
            #Print message if successfully saved to output_path
        print(f"File saved as '{output_path}'")
    else:
    	#Prints an error message with status code
        print("Error occurred while retrieving the file:", response.status_code)


#Define the function
def merge_fasta_files(fasta_file_path, crap_file_path, output_file_path):
	#Opens the fasta_file_path file in read mode ('r') using a context manager
    with open(fasta_file_path, 'r') as file:
    	#Reads the contents of the opened fasta_file_path file and assigns it to the variable fasta_content
        fasta_content = file.read()

    #Opens the crap_file_path file in read mode ('r') using a context manager
    with open(crap_file_path, 'r') as file:
    	#Reads the contents of the opened crap_file_path file and assigns it to the variable crap_content
        crap_content = file.read()

    #splits the crap_content string into a list of entries based on the ">" delimiter. 
    #Each entry represents a sequence in the FASTA format
    crap_entries = crap_content.split(">")

    #Starts a loop that iterates over each entry in the crap_entries list
    for entry in crap_entries:
    	#Checks if the current entry is empty or consists only of whitespace characters. 
    	#If it is empty, the loop proceeds to the next iteration using the continue statement.
        if not entry.strip():
            continue
        
        #Splits the current entry into a list of lines based on the newline character ("\n")
        lines = entry.split("\n")
        #Assigns the first line of the entry to the variable header. 
        #This line is assumed to contain the header information of the sequence
        header = lines[0]
        #Joins the remaining lines (starting from the second line) of the entry into a single string, representing the sequence. 
        #The empty string ('') is used as the separator between lines.
        sequence = ''.join(lines[1:])

        #Appends the merged content of each entry to the fasta_content string. 
        #The ">" symbol, header, and sequence are formatted as a single string.
        fasta_content += f">{header}\n{sequence}\n"
    
    #Opens the output_file_path file in write mode ('w') using a context manager
    with open(output_file_path, 'w') as file:
    	#Writes the contents of the fasta_content string to the opened output_file_path file
        file.write(fasta_content)

#Specify URLS and file names to be used
fasta_url = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28proteome%3AUP000005640%29%29'
crap_url = 'http://ftp.thegpm.org/fasta/cRAP/crap.fasta'
fasta_file_path = "HRP.fasta"
crap_file_path = "crap.fasta"
output_file_path = "output.fasta"

# Download FASTA file
download_file(fasta_url, fasta_file_path)

# Download contaminant file
download_file(crap_url, crap_file_path)

# Merge FASTA files into one file
merge_fasta_files(fasta_file_path, crap_file_path, output_file_path)
