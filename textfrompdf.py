# to extract the text from pdf
# install pypdf2 through your terminal using pip install pypdf2

import PyPDF2
# use pdfreader to read the content of the pdf
reader = PyPDF2.PdfReader('table.pdf')

# to extract the content in the page use extract_text

extracted = ""
for i in range(1,2):
    extracted = reader.pages[i].extract_text()
# to display the extracted data we will make the new text file
# and store all the data
with open("text.txt", "w", encoding='utf-8') as data_extracted:
    data_extracted.write(extracted)