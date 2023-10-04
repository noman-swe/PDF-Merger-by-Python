import PyPDF2 as PDF

myPdfFiles = ["1.pdf", "2.pdf"]

merger = PDF.PdfMerger()

for filename in myPdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PDF.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')
