# tabula might be useful in general: https://towardsdatascience.com/scraping-table-data-from-pdf-files-using-a-single-line-in-python-8607880c750?gi=bcc48106d7f9
import textract  # pip3 install textract

from os import listdir
from os.path import isfile, join


def main():
    print('\nFor copy-paste convenience, \ndouble-click and copy:\n')
    show_PDFs_in_current_directory()

    file_name = file_prompt()

    text = textract.process(file_name)
    pages = split_into_PDF_pages(text)
    print(f'\nPages: {len(pages)}\n')


def show_PDFs_in_current_directory():
    pdf_file_names = [f for f in listdir('.') if isfile(
        join('.', f)) and f.endswith('.pdf')]
    print('\n'.join(pdf_file_names))


def file_prompt():
    file_name = ''
    try:
        # Python 3:
        file_name = input('\nPDF file name?\n')
    except:
        # Python 2:
        file_name = raw_input('\nPDF file name?\n')
    return file_name


def split_into_PDF_pages(text):
    new_page_character = r'\x0c'
    pages = str(text).split(new_page_character)
    return pages


def show_stats(text):
    pages = split_into_PDF_pages(text)
    print(f'\nPages: {len(pages)}\n')


main()
