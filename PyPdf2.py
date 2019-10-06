import PyPDF2
fileURL="./pdf_name.pdf
pdfFileObj = open(fileURL, 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pageObj = pdfReader.getPage(0) 
string=pageObj.extractText()
print(string)
