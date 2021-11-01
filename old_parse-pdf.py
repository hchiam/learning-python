# (see the newer parse-pdf.py)

# https://automatetheboringstuff.com/chapter13
# pip3 install PyPDF2
import PyPDF2
import re

pdf_path = '...pdf'
pdf_file = open(pdf_path, 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(1)
page_content = page.extractText()  # .encode('utf-8')
attempted_keys_regex = '(\d ?\) ?To .+\n.+\n.+)'
attempted_MV_regex = '(".+?[#|"]?.+?\(.+?\))'  # use with re.DOTALL
print(re.findall(attempted_keys_regex, page_content))
print('\n\n\n'.join(re.findall(attempted_MV_regex, page_content, re.DOTALL)))

# for page_number in range(number_of_pages):
# page = read_pdf.getPage(page_number)
# page_content = page.extractText().encode('utf-8')
# ResSearch = re.search('verse', page_content)
# print(ResSearch)
