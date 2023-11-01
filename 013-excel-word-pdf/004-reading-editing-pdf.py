import PyPDF2, os

address = 'C:\\Users\\Public\\code\\automate-with-python\\013-excel-word-pdf'

os.chdir(address)

pdfFile1 = open('invent-your-games.pdf', 'rb') # rb for reading binary
pdfFile2 = open('automate-with-python.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfReader(pdfFile1)
pdf_reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(pdf_reader1.pages)):
    page = pdf_reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(pdf_reader2.pages)):
    page = pdf_reader2.pages[pageNum]
    writer.add_page(page)

output_combined_books = open('combined-books.pdf', 'wb')

writer.write(output_combined_books)

output_combined_books.close()
pdfFile1.close()
pdfFile2.close()