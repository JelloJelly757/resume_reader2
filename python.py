import pypdf
import re

# open the pdf file
reader = pypdf.PdfReader("resume1.pdf")

# get number of pages
num_pages = len(reader.pages)

# define key terms
string1 = "leadership" #college education
string2 = "university" #skills
string3 = "python" #experiences
string4 = "GPA" #certifications

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

# dictionary filled with words being searched for 
my_dict = {"leadership": 1, "university": 2, "python": 3, "GPA": 4}

# function to get points per pdf 
def get_points_for_pdf(words):
    total_points = 0
    for word in words:
        if word in my_dict:
            total_points += my_dict[word]
    return total_points

# extract text and calculate the score
total_pdf_points = 0 
for page in reader.pages:
    text = page.extract_text()
    words = text.split()  # Split the text into individual words
    total_points = get_points_for_pdf(words)
    print(f"Total points for this page: {total_points}")
    total_pdf_points += total_points 

# makes point total for the whole pdf    
print(f"Total points for whole pdf: {total_pdf_points}")