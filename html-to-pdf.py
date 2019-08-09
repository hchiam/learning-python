# https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
# https://pypi.org/project/pdfkit/

# brew install Caskroom/cask/wkhtmltopdf
# pip install pdfkit

import pdfkit
pdfkit.from_url('https://www.google.com', 'website-example.pdf')
pdfkit.from_file('test.html', 'file-example.pdf')
pdfkit.from_string('Hello!', 'string-example.pdf')
