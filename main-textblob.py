from textblob import TextBlob # PIP required (preferred installer program)
from pypdf import PdfReader # PIP required (pip install pypdf[full])
import os

my_file = (r"Projects\Sentiment analysis\Sentiment-analysis-example-2.pdf")

# SETUP ENGINE
if os.path.splitext(my_file)[1] == '.pdf':
    reader = PdfReader(my_file)
    page = reader.pages[0]
    data = page.extract_text()

if os.path.splitext(my_file)[1] == '.txt':
    with open(my_file, 'r') as file:
        data = file.read()
        data = data.replace('\n', '')
        data = '\n'.join([line for line in data.split('\n') if not line.startswith('#')])

# ANALYSIS ENGINE
polValue = TextBlob(data).sentiment.polarity
subValue = TextBlob(data).sentiment.subjectivity

# Polarity (-1:+1)
# Value of example = -0.008341076267905536
# -1 (Negative statement)
# 0 (Neutral statement)
# +1 (Positive statement)
print("Polarity of Text is: {}.".format(polValue))

# Subjectivity (0:+1)
# Value of example = 0.4121157568718545
# 0.0 (Objective statement)
# 0.5 ?
# 1.0 (Subjective statement)
print("Subjectivity of Text is: {}.".format(subValue))
