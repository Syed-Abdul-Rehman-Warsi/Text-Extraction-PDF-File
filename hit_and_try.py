from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pathlib2 import Path
import re
import os



def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


paragraph = "Abstract"
def abstractExtraction(text,paragraph):

    count = 0
    para=""
    text=text.replace('\n\n+', '\n')
    text=text.replace('\s\s\s+', '\n')
    for i in re.split(r'\n+', text):
        p = re.compile('(?<!\S)'+paragraph, re.IGNORECASE)
        p1 = re.compile('abstract')
        if(str(p1.match(i)))=='None':
            if str(p.match(i))!='None':
                count=1
            if count == 1:
                if str(re.compile('\d' + '.*' + '\s*' + 'Introduction', re.IGNORECASE).match(i))!='None':
                    x = re.findall("Keywords.*", para)
                    s = ''
                    print(s.join(x))
                    print(x, s)
                    return para
                elif str(re.compile('X|IV|V?I{0,3}' + '.*' + '\s*' + 'Introduction', re.IGNORECASE).match(i))!='None':
                    x = re.findall("Keywords.*", para)
                    s = ''
                    print(s.join(x))
                    print(x,s)
                    return para
                else:
                    para =para+i
                    continue

    if(len(para)>1000):
        return 'None'
    else:
        x = re.findall("Keywords.*", para)
        s = ''
        print(s.join(x))
        print(x, s)
        return para

a = (convert_pdf_to_txt('123.pdf'))
print(abstractExtraction(a, paragraph))
#d = '123.pdf'
#e = '1234.pdf'
#w = (convert_pdf_to_txt(d))
#z = (convert_pdf_to_txt(e))
#print(z)

#a = abstractExtraction(w, paragraph)
#print(a)

#b = abstractExtraction(z, paragraph)
#print(b)

#x = re.findall("Keywords.*", b)
#print(x)


#with Path('warsi.txt').open(mode='w') as output_file:
   # output_file.write(a)

#with Path('warsi1.txt').open(mode='w') as output_file:
    #output_file.write(b)

'''parag = ''
for i in b:
    if i == ',' or i == '.':
        parag = parag + "\n"
    else:
        parag = parag + i
    with Path('warsi2.txt').open(mode='w') as output_file:
        output_file.write(parag)

print(parag)'''




# ['Keywords:  Metaheuristic,  genetic  algorithm,  Tabu  Search, Neural Network, WEKA. ']

