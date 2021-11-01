import pdfplumber  # pip3 install pdfplumber

from os import listdir
from os.path import isfile, join
import re

from read_write_file import write, append, read


def main():
    print('\nFor copy-paste convenience, \ndouble-click and copy:\n')
    show_PDFs_in_current_directory()

    file_name = file_prompt()

    page_texts = get_page_texts_in_pdf(file_name)

    write('backup.txt', '\n'.join(page_texts))
    txt_string = read('backup.txt')
    lines = txt_string.split('\n')

    hst_lines = []
    rebate_lines = []
    total_lines = []
    for index, line in enumerate(lines):
        hst_util = 'HST on Gas '
        hst_hydro = 'Harmonized Sales Tax on $'
        hst_hydro_new = 'HST ('
        if hst_util in line or hst_hydro in line or hst_hydro_new in line:
            # HST
            hst_lines.append(get_number_at_end_of_line(line))

        rebate_hydro = 'Electricity Rebate'
        if rebate_hydro in line:
            # rebate
            rebate_lines.append(get_credit_at_end_of_line(line))

        total_util_g_w = 'Total Gas & Water Charges'
        total_util_s = 'Total  Stormwater Rate Charges'
        if total_util_g_w in line:
            # total, including HST
            total_lines.append('GW ' + get_number_at_end_of_line(line))
        if total_util_s in line:
            # total, including HST
            total_lines.append(' S ' + get_number_at_end_of_line(line))

        total_hydro = 'PAYABLEONOR'  # always line above
        total_hydro_new = 'What Do I Owe?'  # always line above
        if total_hydro in line or total_hydro_new in line:
            # total, including HST
            next_line = lines[index+1]
            total_lines.append(get_total_for_hydro_new(next_line))

    write('_hst.txt', '\n'.join(hst_lines))
    write('_rebate.txt', '\n'.join(rebate_lines))
    write('_total.txt', '\n'.join(total_lines))


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


def get_page_texts_in_pdf(file_name):
    pdf = pdfplumber.open(file_name)
    pages = pdf.pages
    page_texts = [page.extract_text() for page in pages]
    pdf.close()
    return page_texts


def get_tables_in_page(page):
    page_tables = page.extract_tables()
    return page_tables


def print_rows_in_table(table):
    for row in table:
        print(row)
    print('-------')  # dividing line
    return table


def get_pattern_match(regex_string, text):
    pattern = re.compile(regex_string)
    return pattern.findall(text)[0]


def get_number_at_end_of_line(line):
    return get_pattern_match(' ?(\d*\.\d*)$', line)


def get_credit_at_end_of_line(line):
    return get_pattern_match(' ?(\d*\.\d*) ?CR$', line)


def get_total_for_hydro_new(line):
    return get_pattern_match('\$(\d*\.\d*)($| )', line)[0]
    # e.g. extra [0] to look into [('67.53', '')]


main()
