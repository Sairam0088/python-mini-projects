# pdf compressor using python
import PyPDF2

def compress_pdf(input_path, output_path):
    with open(input_path, "rb") as inputfile:
        reader = PyPDF2.PdfReader(inputfile)
        writer = PyPDF2.PdfWriter()
    
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.compress_content_streams()
            writer.add_page(page)
        
        with open(output_path, "wb") as outputfile:
            writer.write(outputfile)
            print("Pdf Compressed successfully")

input_path = "pdf_14.pdf" #14.5 mb
output_path = "compressed_pdf1.pdf" #7.9 mb
compress_pdf(input_path, output_path)
            
        