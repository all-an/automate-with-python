import docx

address = 'C:\\Users\\Public\\code\\automate-with-python\\013-excel-word-pdf'

file1 = '\\demo2.docx'

my_file = address + file1

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragr in doc.paragraphs:
        fullText.append(paragr.text)
    return '\n'.join(fullText)

print(getText(my_file))