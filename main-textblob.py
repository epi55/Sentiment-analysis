from textblob import TextBlob # PIP required (preferred installer program)
from pypdf import PdfReader # PIP required
import os

my_file = (r"Projects\Sentiment analysis\Sentiment-analysis-example.pdf")

# SETUP ENGINE
if os.path.splitext(my_file)[1] == '.pdf':
    reader = PdfReader(my_file)
    page = reader.pages[0]
    print(page.extract_text())
    #pdf_file = open(my_file, 'rb')
    #pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    #text = ''

    #for page in range(pdf_reader.getNumPageS()):
    #    text += pdf_reader.getPage(page).extractText()

    #with open(my_file, 'w') as file:
    #    file.write(text)

if os.path.splitext(my_file)[1] == '.txt':
    with open(my_file, 'r') as file:
        data = file.read()
        data = data.replace('\n', '')
        data = '\n'.join([line for line in data.split('\n') if not line.startswith('#')])

text = data

# ANALYSIS ENGINE
polValue = TextBlob(text).sentiment.polarity
subValue = TextBlob(text).sentiment.subjectivity

# Polarity (-1:+1)
# Value of example = -0.008341076267905536
# -1 (Negative statement)
# +1 (Positive statement)
print("Polarity of Text is: {}.".format(polValue))

# Subjectivity (0:+1)
# Value of example = 0.4121157568718545
# 
print("Subjectivity of Text is: {}.".format(subValue))
