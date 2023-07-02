import PyPDF2

pdfReader = PyPDF2.PdfReader(open('PdfSample.pdf', 'rb'))
watermarkReader = PyPDF2.PdfReader(open('Watermark.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(pdfReader.pages)):
  page = pdfReader.pages[i] 
  page.merge_page(watermarkReader.pages[0])
  output.add_page(page)

  with open('Watermarked.pdf', 'wb') as file:
    output.write(file)
  