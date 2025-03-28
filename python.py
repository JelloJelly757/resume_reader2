import pypdf
import re
resumeNameList=[]
pointArray=[]
for x in range(6):
    resumeNameList.append(f"resume{x+1}.pdf")
print(resumeNameList)

for pdfName in resumeNameList:
    
    # open the pdf file
    reader = pypdf.PdfReader(pdfName)

    # get number of pages
    num_pages = len(reader.pages)

    # define key terms
    string1.lower() == "leadership".lower() #college education
    string2.lower() == "university".lower() #skills
    string3.lower() == "python".lower() #experiences
    string4.lower() == "GPA".lower() #certifications

    # extract text and do the search
    for page in reader.pages:
        text = page.extract_text() 
        # print(text)
        res_search = re.findall(string1, text)
        print(res_search)
        res_search = re.findall(string2, text)
        print(res_search)
        res_search = re.findall(string3, text)
        print(res_search)
        res_search = re.findall(string4, text)
        print(res_search)

    my_dict = {"leadership":   1, "university": 2, "python": 3, "GPA": 4}

    def get_points_for_pdf(words):
        total_points = 0
        for word in words:
            if word in my_dict:
                total_points += my_dict[word]
        return total_points

    total_pdf_points = 0
    # extract text and calculate the score
    for page in reader.pages:
        text = page.extract_text()
        words = text.split()  # Split the text into individual words
        total_points = get_points_for_pdf(words)
        print(f"Total points for this page: {total_points}")
        total_pdf_points += total_points
    print(f"Total points for this PDF: {total_pdf_points}")
    pointArray.append(total_pdf_points)
    pointArray.append("|")
print(pointArray)