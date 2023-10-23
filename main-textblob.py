# SETUP
import os

### PIP required (preferred installer program)
from textblob import TextBlob # pip install textblob
from pypdf import PdfReader # pip install pypdf[full]
import pandas as pd # pip install pandas
import numpy as np # pip install pandas
from openpyxl import load_workbook

# ENGINES
def extractEngine(documentPath, filename):
    data = ''

    if os.path.splitext(documentPath)[1] == '.pdf':
        reader = PdfReader(documentPath)
        fileLength = len(reader.pages)
        for i in range(fileLength):
            page = reader.pages[i]
            pageExtract = page.extract_text()
            data += pageExtract

    if os.path.splitext(documentPath)[1] == '.txt':
        with open(documentPath, 'r') as file:
            data = file.read()
            data = data.replace('\n', '')
            data = '\n'.join([line for line in data.split('\n') if not line.startswith('#')])
    
    # TEST
    print("##### extractEngine test #####")
    testPrint()

    analysisEngine(data, documentPath)

def analysisEngine(data, documentPath):
    polValue = TextBlob(data).sentiment.polarity
    subValue = TextBlob(data).sentiment.subjectivity

    # TEST
    print("##### analysisEngine test #####")
    testPrint()

    updateEngine(documentPath, polValue, subValue)

    ## PANDAS
    #output_data = pd.DataFrame({"Document": [filename], "polValue": [polValue], "subValue": [subValue]})
    #output_data.to_excel("{}\output_data.xlsx".format(outputFolderPath), index=False)

    #print("# {} \n## Polarity: {} \n## Subjectivity: {}\n".format(filename, polValue, subValue))
    
    ## SENTINMENT ANALYSIS INFO
    # Polarity (-1:+1)
    # Value of example = -0.008341076267905536
    # -1 (Negative statement)
    # 0 (Neutral statement)
    # +1 (Positive statement)
    #print("Polarity of data is: {}.".format(polValue))

    # Subjectivity (0:+1)
    # Value of example = 0.4121157568718545
    # 0.0 (Objective statement)
    # 0.5 ?
    # 1.0 (Subjective statement)
    #print("Subjectivity of data is: {}.".format(subValue))

def updateEngine(documentPath, polValue, subValue):
    workbookName = 'output_data.xlsx'
    wb = load_workbook(workbookName)
    page = wb.active

    new_analysis = [[documentPath, polValue, subValue]]

    for info in new_analysis:
        page.append(info)

    wb.save(filename=r"Projects\Sentiment analysis\Examples\output_data.xlsx")

    # TEST
    print("##### updateEngine test #####")
    testPrint()

# TEST FUNC
def testPrint():
    my_file = (r"Projects\Sentiment analysis\Examples\test1.txt")
    with open(my_file, 'r') as file:
        data = file.read()
        print(data)

# RUN
docFolderPath = r"Projects\Sentiment analysis\Examples"
outputFolderPath = r"Projects\Sentiment analysis\Outputs"

for filename in os.listdir(docFolderPath):
    if filename.endswith((".txt", ".pdf")):
        documentPath = (r"{}\{}".format(docFolderPath, filename))
        
        # TEST
        print("###############\n# {}\n# {}\n# {}\n# {}\n###############".format(filename, docFolderPath, outputFolderPath, documentPath)) # TEST
        
        # TEST
        print("##### INIT test #####")
        testPrint()

        extractEngine(documentPath, filename)
