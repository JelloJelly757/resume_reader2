import pypdf
import re
resumeNameList=[]
pointArray=[]
for x in range(6):
    resumeNameList.append(f"resume{x+1}.pdf")
print(resumeNameList)

# loop through each pdf file
for pdfName in resumeNameList:
    
    # open the pdf file
    reader = pypdf.PdfReader(pdfName)

    # get number of pages
    num_pages = len(reader.pages)

    # define key terms
    string1 = "leadership".lower() #college education
    string2 = "university".lower() #skills
    string3 = "python".lower() #experiences
    string4 = "GPA".lower() #certifications

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

    my_dict = {"leadership": 1, "university": 2, "python": 3, "GPA": 4}

    # function to calculate points for the PDF
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

max_points = max(pointArray[::2])
best_resume_index = pointArray.index(max_points) // 2 

for i in range(0, len(pointArray), 2):
    print(f"Resume {i//2 + 1}: {pointArray[i]} points")

print(f"The best resume is: Resume {best_resume_index + 1} with {max_points} points")

 
#need multi points 
