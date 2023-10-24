# SETUP
import os

### PIP required (preferred installer program)
from textblob import TextBlob # pip install textblob
from pypdf import PdfReader # pip install pypdf[full]
import pandas as pd # pip install pandas
import numpy as np # pip install pandas
from openpyxl import load_workbook

# ENGINES
def extractEngine(filename, documentPath):
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
    
    return data
#    analysisEngine(filename, data)

#def analysisEngine(filename, data):
#    polValue = TextBlob(data).sentiment.polarity
#    subValue = TextBlob(data).sentiment.subjectivity

    #updateEngine(filename, polValue, subValue)

    ## PANDAS
#    output_data = pd.DataFrame({"Document": [filename], "polValue": [polValue], "subValue": [subValue]})
#    output_data.to_excel(r"Projects\Sentiment analysis\Outputs\output_data.xlsx", sheet_name="tester")

#    print("# {} \n## Polarity: {} \n## Subjectivity: {}\n".format(filename, polValue, subValue))
    
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

# RUN
docFolderPath = r"Projects\Sentiment analysis\Examples"
outputFolderPath = r"Projects\Sentiment analysis\Outputs"

all_data = pd.DataFrame(columns=["Document", "polValue", "subValue"])

for filename in os.listdir(docFolderPath):
    if filename.endswith((".txt", ".pdf")):
        documentPath = os.path.join(docFolderPath, filename)
        data = extractEngine(filename, documentPath)
        polValue = TextBlob(data).sentiment.polarity
        subValue = TextBlob(data).sentiment.subjectivity

        all_data = pd.concat([all_data, pd.DataFrame({"Document": [filename], "polValue": [polValue], "subValue": [subValue]})], ignore_index=True)

output_file = os.path.join(outputFolderPath, "output_data.xlsx")
all_data.to_excel(output_file, sheet_name="tester", index=False)

print("Data saved to:", output_file)
