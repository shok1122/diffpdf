import sys
import glob
import pprint

from fuzzywuzzy import fuzz

from pdf_reader import PdfReader

def calc(path_file1, path_file2):

    pdf1 = PdfReader()
    pdf2 = PdfReader()

    pdf1.open(path_file1)
    pdf2.open(path_file2)

    content1 = pdf1.get_text()
    content2 = pdf2.get_text()

    score = fuzz.ratio(content1, content2)

    return score

def calc_r(path_dir):

    files = glob.glob(path_dir + '/*.pdf')

    result = {}
    for f in files:
        result[f] = {}

    worst = {
        'score': 0,
        'file1': '',
        'file2': ''
    }

    blacklist = []

    for i, f1 in enumerate(files):
        for f2 in files[i+1:]:
            score = calc(f1, f2)

            if worst['score'] < score:
                worst['score'] = score
                worst['file1'] = f1
                worst['file2'] = f2

            if 90 <= score:
                blacklist.append( { 'file1': f1, 'file2': f2, 'score': score } )

            result[f1][f2] = score

    return blacklist, worst, result


if __name__ == '__main__':

    dir1 = sys.argv[1]

    blacklist, worst, result = calc_r(dir1)

    print('-------------------------')
    print(' WARNING')
    print('-------------------------')
    pprint.pprint(blacklist)

    print('-------------------------')
    print(' WORST')
    print('-------------------------')
    pprint.pprint(worst)

    print('-------------------------')
    print(' RESULT')
    print('-------------------------')
    pprint.pprint(result)

