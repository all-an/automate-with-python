import PyPDF2, os

address = 'C:\\Users\\Public\\code\\automate-with-python\\013-excel-word-pdf'

os.chdir(address)

pdfFile = open('invent-your-games.pdf', 'rb') # rb for reading binary

pdf_reader = PyPDF2.PdfReader(pdfFile)

print(len(pdf_reader.pages))

page = pdf_reader.pages[77]

print(page.extract_text())