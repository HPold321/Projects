# Extracting Tables from PDF using Python Libraries… a Documentation.


In this I used google Colab to try out the solutions. 
- STEP 1> Upload the PDF file to google docs manually. This pdf doc can have both text and tables. 
- STEP 2> Mount the google drive to google colab using…

      from google.colab import drive
      drive.mount('/content/drive')

- STEP 3> Check that the pdf file is accessible from the colab .ipynb file using… 

      !ls "/content/drive/My Drive/"


The first thing to do after that is to install libraries…I used pyPDF and the code I used was

      !pip install pypdf
      import pypdf

I first tried to extract text from the pdf doc to a .txt file..
import PyPDF2


    def extract_text_from_pdf(pdf_path, txt_path):
       with open(pdf_path, 'rb') as pdf_file:
           pdf_reader = PyPDF2.PdfReader(pdf_file)
           num_pages = len(pdf_reader.pages)


       with open(txt_path, 'w', encoding='utf-8') as txt_file:
           for page_num in range(num_pages):
               page = pdf_reader.pages[page_num]
               text = page.extract_text()
               txt_file.write(text)
               
    pdf_path = "/content/drive/My Drive/paper.pdf"
    txt_path = "/content/drive/My Drive/paper.txt"
    extract_text_from_pdf(pdf_path, txt_path)

**OBSERVATIONS:**
- The code worked and a paper.txt file was created in the google drive. 
- All the text in it was left indented, the tables (eg. contents in TOC) data was printed as ordinary text. 
- No formatting (including headers, footers, subscripts, page nos. Was printed.

The method to extract tables from PDF and one that actually worked was using Tabula. 

    from tabula import read_pdf
    from tabulate import tabulate
    import pandas as pd


    # Read tables from pdf file
    dfs = read_pdf("/content/drive/My Drive/paper.pdf", pages="all")
    
    
    # Save each table as CSV in Google Drive
    for i, df in enumerate(dfs):
       df.to_csv(f"/content/drive/My Drive/Table_{i+1}.csv", index=False)
       print("Tables are saved into drive")
    
    
    # print each table
    for i, df in enumerate(dfs):
       print(f"Table {i+1}:")
       print(tabulate(df, headers='keys', tablefmt='psql'))
**OBSERVATIONS:**
- ‘Tables are saved into drive’ is printed for every table saved into drive.
- Tables are saved as ‘Table_1.csv’ etc. into the drive. These tables are not formatted.
- Tables are also printed in the output area.
- Many tables are missing from the output area including TOC. This may be because of image incorporation and margins in certain areas of the PDF. 
- This margin not being defined also causes many indented texts to be scanned as 1 column tables by tabula. 
By far this is the fastest method to extract tables from a PDF file. This is around 6x faster than other methods including Camelot. 

The method that shows clear results with proper whitespaces is pdfPlumber…

    !pip install pdfplumber
    # Import necessary libraries
    import pdfplumber
    import pandas as pd
    
    
    # Mount Google Drive to access PDF file if it's stored there
    from google.colab import drive
    drive.mount('/content/drive')
    
    
    # Path to your PDF file
    pdf_path = "/content/drive/My Drive/paper.pdf"
    
    
    # Function to extract tables from PDF
    def extract_tables_from_pdf(pdf_path):
       tables = []
       with pdfplumber.open(pdf_path) as pdf:
           for page in pdf.pages:
               tables.extend(page.extract_tables())
       return tables
    
    
    # Extract tables
    tables = extract_tables_from_pdf(pdf_path)
    
    
    # Convert tables to Pandas DataFrame
    dfs = []
    for table in tables:
       df = pd.DataFrame(table[1:], columns=table[0])
       dfs.append(df)
    
    
    # Convert tables to Pandas DataFrame and print
    for i, table in enumerate(tables):
       df = pd.DataFrame(table[1:], columns=table[0])
       print(f"Table {i+1}:")
       print(df)
       print("\n")
**OBSERVATION:**
- The tables are not formatted. Only some tables have a clear header. 
- This table shows null values. 
- It does not take most indented texts as tables, which makes it better than tabula. 
- This is still not very accurate and is slower in comparison to tabula. \
- One plus is that pdfPlumber has specific methods that allow us to extract both text and tables simultaneously by defining the layout and margins. 

Extracting tables using PDFminer does not always work. 

    ! pip install pdfminer-six
    import pdfminer
    from pdfminer.high_level import extract_text
    
    
    # Path to your PDF file
    pdf_path = "/content/drive/My Drive/paper.pdf"
    # Extract tables
    tables = extract_text(pdf_path)
    print(tables)
**OBSERVATIONS:**
- This method streams truncated output. 
- It shows most numerical values accurately. 
- Shows each value in a new line instead of formatted white spaces. 
- The indentation in the output is different based on the type of data. 
- Some indented lines in pdf file are taken as table columns. No headers are shown.
