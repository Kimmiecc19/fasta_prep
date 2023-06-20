#This Python code imports the requests module, which allows making HTTP requests 
#Downloads the HRP from UniProt and saves it as HRP.fasta
#To get URL: Go to Uniprot HRP, click on download, select "fasta" "No" (for compression), copy URL (not the one in chunks)
#This code imports the requests module, constructs a URL to query the UniProt database for a specific proteome's protein sequences in FASTA format, and retrieves those sequences as a string using an HTTP GET request.
#Put commands into script called get_fasta.py
#Run: python get_fasta.py


#The requests library is imported to make HTTP requests.
import requests

#The url variable contains the URL from which the FASTA data will be retrieved.
url = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28proteome%3AUP000005640%29%29'

#The requests.get(url) sends an HTTP GET request to the specified URL.
response = requests.get(url)


#The response is checked using the status_code attribute. If it is 200 (indicating a successful response), the FASTA data is retrieved using response.text.
#The with open('output.fasta', 'w') as file statement opens a new file called 'output.fasta' in write mode.
#The retrieved FASTA data is written to the file using file.write(fasta_data).
#Finally, a message is printed to indicate that the FASTA file has been saved as 'output.fasta'.
if response.status_code == 200: #The server successfully answered the http request
    fasta_data = response.text
    with open('HRP.fasta', 'w') as file:
        file.write(fasta_data)
        print("FASTA file saved as 'HRP.fasta'")
else:
    print("Error occurred while retrieving the FASTA file:", response.status_code)


