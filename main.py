import os
import PyPDF2

def extractString(pdfs, searchCriteria):
    matchedFiles = []
    
    for pdfFile in pdfs:
        with open(pdfFile, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text and searchCriteria in text:
                    matchedFiles.append(pdfFile)
                    break
    
    return matchedFiles

def main():
    directory="C:\\tmp\\"
    detectedPDFs=[]

    for directoryItems in os.listdir(directory):
        if directoryItems.endswith(".pdf"):
            detectedPDFs.append(directory+directoryItems)
    searchCriteria = "test"

    matchedFiles = extractString(detectedPDFs, searchCriteria)

    if matchedFiles:
        print("Files containing the string:")
        for file in matchedFiles:
            print(file)
    else:
        print("No files found containing the string.")

if __name__ == "__main__":