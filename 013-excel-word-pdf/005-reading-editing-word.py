import docx

address = 'C:\\Users\\Public\\code\\automate-with-python\\013-excel-word-pdf'

file1 = '\\demo.docx'

dir1 = address + file1

document = docx.Document(dir1)

print(type(document))

