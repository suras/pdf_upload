
# coding: utf-8

# In[187]:


import pandas as pd
import numpy as np 
import tabula
import pdfplumber
import re
import sys


# In[188]:


## Tested & Working

file_axis1 = '/Users/Khushboo/Desktop/not_running/unlocked/AXIS/Amruta Sankulkar _BS_YesAMRU867722437_Axis_AXIS BANK  Statement for February  2018-1 (1)_unlocked.pdf'
file_axis2 = '/Users/Khushboo/Desktop/not_running/Balram Rawat_BS_No_Axis_RECENT STATMENT (1).pdf'
file_sbi = '/Users/Khushboo/Desktop/not_running/SBI/Avinash Kumar SINHA _BS_No_SBI_20180409135735XXXXXXX2102.pdf'
file_idfc = '/Users/Khushboo/Desktop/not_running/idfc/Aamirpathan_BS_No_IDFC_IDFC Bank statement as of 05 MAR 2018-1 (1).pdf'
file_yes = "/Users/Khushboo/Downloads/BS_not_working/Yes2.pdf"
file_idbi = '/home/surendar/suren/kaarva/idbi.pdf'
file_citi = '/Users/Khushboo/Downloads/BS_not_working/CITI.pdf'
file_scb = "/Users/Khushboo/Downloads/BS_not_working/SCB.pdf"
file_scb_2 = '/Users/Khushboo/Desktop/not_running/unlocked/YES/Rupin Wadhera_BS_Yes52510720117__eStatement0117IN_2018-01-31_1448_unlocked.pdf'
file_canara = '/Users/Khushboo/Downloads/BS_not_working/CANARA.pdf'
file_kotak_1 = "/Users/Khushboo/Downloads/BS_not_working/kotak1.pdf"
file_kotak_2 = "/Users/Khushboo/Downloads/BS_not_working/kotak2.pdf"
file_kotak_3 = '/Users/Khushboo/Desktop/not_running/unlocked/YES/Pankaj Chauhan _BS_Yes211000630__206723-XXXXXXX-201301 (1)_unlocked.pdf'
file_kotak_4 = '/Users/Khushboo/Downloads/BS_not_working/kotak4.pdf'
file_boi = '/Users/Khushboo/Desktop/New BS/BOI.pdf'
file_equitas = '/Users/Khushboo/Desktop/New BS/equi.pdf'
file_karurvyasa = '/Users/Khushboo/Desktop/New BS/KARUR_VYASA.pdf'
file_federal = '/Users/Khushboo/Desktop/New BS/FEDERAL (2).pdf'
file_syndicate = '/Users/Khushboo/Desktop/New BS/syndicate_bank_tmp.pdf'
file_karnataka = '/Users/Khushboo/Desktop/New BS/karnatakab.pdf'


file_hdfc1 = "/Users/Khushboo/Desktop/not_running/HDFC/Diprojit Das_BS_No_HDFC_112098077_1521798431411 (1).pdf"


# Testing

file_hdfc1 = "/Users/Khushboo/Desktop/not_running/HDFC/Diprojit Das_BS_No_HDFC_112098077_1521798431411 (1).pdf"
file_hdfc3 = '/Users/Khushboo/Downloads/BS_not_working/HDFC3.pdf'


## Issue
file_hdfc3 = '/Users/Khushboo/Downloads/BS_not_working/HDFC3.pdf'

file_icici = "/Users/Khushboo/Downloads/BS_not_working/icici2forrm.pdf"
file_icici_1 = '/Users/Khushboo/Desktop/not_running/ICICIIIIII/Akash Chaubey_BS_Yes34401546157__Statement_MAR2018_312359557-1 (1)_unlocked.pdf'
file_icici_2 = '/Users/Khushboo/Downloads/BS_not_working/ICICI2.pdf'
file_icici_3 = '/Users/Khushboo/Downloads/BS_not_working/ICICI3.pdf'

file_paytm = '/Users/Khushboo/Desktop/New BS/paytm.pdf'

## Yes to Test

## Need Bank Statements:
#Punjab, Bandhan, Andhra, BOB, Union Bank, UCO Bank, Indian Bank, Dena Bank, Bank of Maharashtra, Allahabad Bank,
# Bank of Maharashtra, Central Bank of India, Corporation Bank, Indian Overseas Bank, Oriental Bank of Commerce,
# United Bank of India, Vijaya Bank, Punjab & Sind Bank, UTI Bank , DCB Bank, IndusInd Bank Limited, RBL, South Indian Bank
## List if all banks: https://business.mapsofindia.com/banks-in-india/

# document = file_idbi
# Bank_Name = "IDBI"
# print sys.argv[1]
# print sys.argv[2]
document = sys.argv[2]
Bank_Name = sys.argv[1]

pdf = pdfplumber.open(document)
   


# In[189]:


## 3 All the functions needed to extract the data from pdf are here

#Define a String finder that takes in a regex function and a pdf page and returns the matching string

def matched_string_finder(regex, page, x_tol, y_tol, regex_option):
    text = page.extract_text(x_tolerance=x_tol, y_tolerance=y_tol)
    matched_string = []
    #print (text)
    #print (regex_option)
    if (regex_option == 1):
    
        try:
            matches = re.finditer(regex, text, re.IGNORECASE | re.MULTILINE)
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1
    
                #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                #print ("{match}".format(match = match.group()))
                line_start = match.start()
                line_end = match.end()
                matched_string = match.group()
                #header = header_string.split(" ")
        except:
            pass
    
    if (regex_option == 2): 
        matched_string = []
        matches = re.search(regex, text, re.MULTILINE)
        if matches:
            #print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
            line_start = matches.start()
            line_end = matches.end()
            matched_string = matches.group()
                       
    if (regex_option == 3):
    
        try:
            matches = re.finditer(regex, text, re.IGNORECASE | re.MULTILINE)
            for matchNum, match in enumerate(matches):
                #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                #print ("{match}".format(match = match.group()))
                line_start = match.start()
                line_end = match.end()
                matched_string = match.group()
                break
                #header = header_string.split(" ")
        except:
            pass
    
            
    return matched_string


# Define a String exists or not function that takes in a string and returns true of string exists or else false

def string_exists(string):
    if string == []:
        string_present = False
        #print ("String Present : %r" %string_present)
    else:
        string_present = True
        #print ("String Present : %r" %string_present)
    return string_present

# Define a location finder function that given a pdf page and a string, find the top location and bottom location of the string on the page

def location_finder(page, string, x_tol, y_tol):
    p1 = []
    p1 = page.extract_words(x_tolerance=x_tol, y_tolerance=y_tol)
    #print (p1)
    string_list = string.split(" ")
    string_length = len(string_list)
    #print (string_length)
    top_loc_list = []
    bottom_loc_list = []

    for element in range (0,string_length):
        #print (string_list[element])
        string_element_list = []
        try:
            string_element_list = next((x for x in p1 if x['text'] == string_list[element]), None)
            top_loc = string_element_list['top']
            bottom_loc = string_element_list['bottom']
            #print (top_loc)
            #print (bottom_loc)
            top_loc_list.append(top_loc)
            bottom_loc_list.append(bottom_loc)
            #print (top_loc_list)
            #print (bottom_loc_list)
        except:
            pass
     
    master_table_loc_top = 0
    master_table_loc_top = max(top_loc_list)
    master_table_loc_bottom = page.height
    master_table_loc_bottom = max(bottom_loc_list)
    
    #print (master_table_loc_top)
    #print (master_table_loc_bottom)
    return master_table_loc_top, master_table_loc_bottom

def table_coordinate_finder (page,regex_header, regex_footer, x_tol, y_tol, regex_option):

    table_top = 0
    table_bottom = 0
    header_string_exists = False
    footer_string_exists = False
    
    header_row = matched_string_finder(regex_header, page, x_tol, y_tol, regex_option=3)
    footer_row = matched_string_finder(regex_footer, page, x_tol, y_tol, regex_option)
    
    print (header_row)
    print (footer_row)

    ### Check header or footer is not empty

    
    header_string_exists = string_exists(header_row)
    footer_string_exists = string_exists(footer_row)

    print ("Header String Present : %r" %header_string_exists)
    print ("Footer String Present : %r" %footer_string_exists)

    ### If header is not empty, find the header location as the top location of the table
    if (header_string_exists):
        header_top_loc, header_bottom_loc = location_finder(page, header_row, x_tol, y_tol)
        table_top = header_top_loc

    if (footer_string_exists):
        footer_top_loc, footer_bottom_loc = location_finder(page, footer_row, x_tol, y_tol)
        table_bottom = footer_bottom_loc

    return table_top, table_bottom
    


# In[190]:


#4 Define Headers for all possible bank statements

my_header = {
'KOTAK' : {'9': ['S No.','Date',' ','Description','Additional Info','Amount','Dr / Cr','Balance','Useless'],
           '6': ['Date','Description',' ','Additional Info','Withdrawal (Dr)/Deposit (Cr)','Balance'],
           '5': ['Date','Description','Additional Info','Withdrawal (Dr)/Deposit (Cr)','Balance']},
           
'ICICI' : {'6': ['Date','Mode','Description','Credit','Debit','Balance'],
           '8': ['S No','Date','Transaction Date','Cheque Number','Description','Debit','Credit','Balance']},

'AXIS'  : {'7': ['Date','Useless','Description','Debit','Credit','Balance','Init.Br'],
           '6': ['Date','Description','Debit','Credit','Balance','Useless'],
           '5': ['Date','Description','Debit','Credit','Balance']},

'CANARA': {'7': ['Date','Value Date','Useless','Description','Debit','Credit','Balance']},

'CITI':   {'5': ['Date','Description','Debit','Credit','Balance']},
           
'HDFC':   {'7': ['Date','Description','Additional Info','Value Dt','Debit','Credit','Balance'],
           '6': ['Date','Description','Additional Info','Value Dt','Debit','Balance']},
    
'IDBI':   {'9': ['S No','Date','Value Date','Description','Additional Info','Dr / Cr','Useless','Amount','Balance'],
           '8': ['S No','Date','Value Date','Description','Dr / Cr','Useless','Amount','Balance'],
           '10': ['S No','Date','Value Date','Description','Useless','Useless','Dr / Cr','Useless','Amount','Balance'],
           '11': ['S No','Date','Value Date','Description','Useless','Useless','Useless','Dr / Cr','Useless','Amount','Balance']},
           
'IDFC':   {'6': ['Date','Description','Additional Info','Debit','Credit','Balance']},

'SBI':    {'7': ['Date','Value Date','Description','Additional Info','Debit','Credit','Balance']},
           
'SCB':    {'7': ['Date','Value Date','Description','Cheque','Credit','Debit','Balance']},
           
'YES':    {'6': ['Date','Value Date','Description','Debit','Credit','Balance']},

'BOI':  {'7': ['S No','Date','Description','Useless','Debit','Credit','Balance']},

'SYNDICATE': {'6': ['Date','Description', 'Cheque Number', 'Debit', 'Credit','Balance']},

'FEDERAL': {'9': ['Date','Description','Remarks','Additional Info','Details','Debit','Credit','Balance','Useless'],
            '10': ['Date','Description','Remarks','Additional Info','Useless','Details','Debit','Credit','Balance','Useless']}, 
    
'KRVYASA': {'8': ['Date','Value Date','Useless','Cheque Number','Description','Debit','Credit','Balance']},     

'KARNATAKA': {'6': ['Date','Description','Useless','Debit','Credit','Balance'],
              '5': ['Date','Description','Debit','Credit','Balance']},
    
'EQUITAS': {'6': ['Date','Additional Info','Description','Debit','Credit','Balance']},

'PAYTM': {'6': ['Date','Description','Additional Info','Additional Info','Amount','Balance'],
          '5': ['Date','Description','Additional Info','Amount','Balance'],
          '4': ['Date','Description','Amount','Balance']}

}


# In[191]:


## Define if tabula_method would be True for Lattice. 

tset_1 = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
}


tset_2 = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "text",
}


extraction_method = {
    'AXIS': {'Method': 'Tabula', 'Lattice': True, 'table_settings' : tset_1,'Bottom Padding' : 20},
    'SBI' : {'Method': 'Plumber', 'Lattice': False, 'table_settings' : tset_1,'Bottom Padding' : 40},
    'IDFC' : {'Method': 'Tabula', 'Lattice': True, 'table_settings' : tset_1,'Bottom Padding' : 40},
    'YES': {'Method': 'Tabula', 'Lattice': False, 'table_settings' : tset_1,'Bottom Padding' : 20},
    'IDBI': {'Method': 'Tabula', 'Lattice': False, 'table_settings' : tset_1,'Bottom Padding' : 20},
    'HDFC': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 0},
    'CITI': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 0},
    'SCB': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 0},
    'CANARA': {'Method': 'Plumber', 'Lattice': True,'table_settings' : tset_1,'Bottom Padding' : 20},
    'ICICI': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'KOTAK': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 10},
    'KRVYASA': {'Method': 'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'FEDERAL': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'SYNDICATE': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'EQUITAS': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'BOI': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'KARNATAKA': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 20},
    'PAYTM': {'Method':  'Tabula', 'Lattice': False,'table_settings' : tset_1,'Bottom Padding' : 0}
}


#extraction_method[Bank_Name]['table_settings']


# In[192]:


## 5 All the functions needed to clean the data extracted to get to the standard form are here


## Define a function that assigns the header to the data table

def assign_header(df, bank_name):
    len_of_header = str(page_df.shape[1])
    print(len_of_header)
    header = my_header[bank_name][len_of_header]
    df.columns = header
    df_w_headers = df
    return df_w_headers

def rolling_group(val):
    if pd.notnull(val): rolling_group.group +=1 #pd.notnull is signal to switch group
    return rolling_group.group

def joinFunc(g,column):
    col =g[column]
    joiner = "/" if column == "Action" else " "
    s = joiner.join([str(each) for each in col if pd.notnull(each)])
    s = re.sub("(?<=&)"+joiner," ",s) #joiner = " "
    s = re.sub("(?<=-)"+joiner,"",s) #joiner = ""
    s = re.sub(joiner*2,joiner,s)    #fixes double joiner condition
    return s


## Function that splits the CR/DR amount in two different columns when the columns name is 'Withdrawal (Dr)/Deposit (Cr)'

def split_cr_dr(df):
    data_CR = df[df['Withdrawal (Dr)/Deposit (Cr)'].str.contains('Cr', na = False)]
    data_DR = df[df['Withdrawal (Dr)/Deposit (Cr)'].str.contains('Dr', na = False)]
    dfCR = data_CR.rename(columns={'Withdrawal (Dr)/Deposit (Cr)': 'Credit (Cr)',})
    dfDR = data_DR.rename(columns={'Withdrawal (Dr)/Deposit (Cr)': 'Debit (Dr)',})
    df_tot = pd.concat([dfDR,dfCR], ignore_index=False)
    page_split_df = df_tot[['Date', 'Description', 'Debit (Dr)', 'Credit (Cr)','Balance']]
    page_split_df.sort_index(inplace=True)
    
    # define words that we may want to remove (Cr, Dr)
    remove_words = ['(Cr)', '(Dr)']
    pat = r'\(.*\)'.format('|'.join(remove_words))
    page_split_df['Debit'] = page_split_df['Debit (Dr)'].str.replace(pat, '')
    page_split_df['Credit'] = page_split_df['Credit (Cr)'].str.replace(pat, '')
    page_split_df['Balance_new'] = page_split_df['Balance'].str.replace(pat, '')
    page_split_df.drop(['Debit (Dr)', 'Credit (Cr)', 'Balance'], axis=1, inplace = True)
    page_split_df.rename(columns={'Balance_new': 'Balance'}, inplace = True)

    return page_split_df  

## Function that splits the CR/DR amount in two different columns when the columns name is Amount and a seperate Cr/Dr column is present

def split_amount(df):
    data_CR = df[df['Dr / Cr'] == 'CR']
    data_DR = df[df['Dr / Cr'] == 'DR']
    dfCR = data_CR.rename(columns={'Amount': 'Credit',})
    dfDR = data_DR.rename(columns={'Amount': 'Debit',})
    df_tot = pd.concat([dfDR,dfCR], ignore_index=False)
    df_tot.sort_index(inplace=True)
    account_split_df = df_tot[['Date','Description', 'Debit', 'Credit','Balance']]
    return account_split_df


# In[193]:


## 4

doc_length = len(pdf.pages)
#print ("This PDF has %d pages" %doc_length)

page_list = []
page = []
x_tol = 3
y_tol = 2

master_data = pd.DataFrame()

for i in range (0, len(pdf.pages)):
    page = pdf.pages[i]
    page_list.append(page)
    
print (page_list)

length = len(page_list)
num = 0
header_page_found = False
    

# for testing purpose only
print (length)
#num = 0
#length = 1

for page_num in range(num,length):
    page = pdf.pages[page_num]
    actual_page = page_num + 1
    print ("We are on page num: %d" %actual_page)
    #print (page.extract_text(x_tolerance=x_tol, y_tolerance=y_tol))
    
    page_df = pd.DataFrame()
    final_page_data = pd.DataFrame()
    padding = 0
    original_header_length = 0
    original_header = pd.DataFrame()
    
    regex_option = 1
    regex_header = r"(?=.*?date\b)(?=.*?balance\b).*$"
    #regex_footer = r"(?=.*?\bTotal\b)(?!\b.*Deposit|.*Withdrawal)(?=.*?\b\d+(\.\d{1,2})\b).*$"
    regex_footer = r"(?:(?:31(\/| |-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/| |-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/| |-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|(?:0?[1-9]|1\d|2[0-8])(\/| |-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})(?=.*?\b\d+(\.\d{1,2})\b).*$"        
    
    try:    
        # Start with the header that contains 'Date' and 'Balance Words' in one line
        # Start with footer that looks for a row containing a Date and a decimal item
            
        table_top, table_bottom = table_coordinate_finder(page, regex_header, regex_footer, x_tol, y_tol, regex_option)
        print ("table_top, table_bottom place1 %d, %d" %(table_top, table_bottom))
        
        # Find footer only once atleast the first time header has been found
        if (table_top > 0):
            header_page_found = True
            header_page = actual_page
            try: 
                original_header = pd.DataFrame(page.crop((0, table_top , page.width, table_top+20)).extract_table())
                #print (header_page_found)
                #print (original_header)
                original_header_length = len(original_header.columns)
            except:
                pass
        
        if (not header_page_found):
            pass
        else:
            if (table_top == 0):
                regex_option = 2
                regex_header_new = r"(?:(?:31(\/| |-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/| |-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/| |-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|(?:0?[1-9]|1\d|2[0-8])(\/| |-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})(?=.*?\b\d+(\.\d{1,2})\b).*$"        
                table_top_new, table_bottom_new = table_coordinate_finder(page, regex_header_new, regex_footer, x_tol, y_tol, regex_option)
                table_top = table_top_new
                #print ("table_top, table_bottom place2 %d, %d" %(table_top, table_bottom))

            if (Bank_Name == 'SCB' or Bank_Name == 'CITI'): 
                if (actual_page < length):
                    regex_option = 1
                    regex_footer_4 = r"^(.*\b(\d{7,})\b).*$"
                    table_top_new, table_bottom_new = table_coordinate_finder(page, regex_header, regex_footer_4, x_tol, y_tol, regex_option)
                    table_bottom_4 = table_bottom_new
                    print ("table_top, table_bottom place4 %d, %d" %(table_top_new, table_bottom_new))
                    table_bottom = max(table_bottom, table_bottom_4)
                elif (actual_page == length):
                    regex_option = 1
                    lp_bot_pad = 10
                    regex_footer_5 = r"(?=.*?\bTotal\b|\bTally\b)(?=.*?\b\d+(\.\d{1,2})\b).*$"
                    table_top_new, table_bottom_new = table_coordinate_finder(page, regex_header, regex_footer_5, x_tol, y_tol, regex_option)
                    table_bottom_5 = table_bottom_new - lp_bot_pad
                    print ("table_top, table_bottom place5 %d, %d" %(table_top_new, table_bottom_5))
                    table_bottom = max(table_bottom, table_bottom_5)


            if (Bank_Name == 'KOTAK' and original_header_length == 8):
                    regex_option = 1
                    table_bottom = page.height

                    regex_footer_6 = r"(?=.*?\bOpening\b)(?=.*?\b\d+(\.\d{1,2})\b).*$"
                    table_top_new, table_bottom_new = table_coordinate_finder(page, regex_header, regex_footer_6, x_tol, y_tol, regex_option)
                    table_bottom_6 = table_bottom_new
                    print ("table_top, table_bottom place6 %d, %d" %(table_top_new, table_bottom_6))

                    if (table_bottom_6 > 0):
                        new_table_bottom = table_bottom_6 - 20
                        table_bottom = min(new_table_bottom, page.height)
            
            if (Bank_Name == 'KARNATAKA' and actual_page == 1) :
                table_top = table_top + 30
            
            # Use Tabula to extract the dataframe of the table from the page and append to the master table df
            # area is specified in following order: top, left, bottom, right
            #print (table_top)
            #table_bottom = page.height
            
            # Extract only when there is some table data on the page i.e table_bottom > 0
            if (table_bottom > 0):
                padding = extraction_method[Bank_Name]['Bottom Padding']
                table_bottom = min(table_bottom + padding, page.height)
                print ("table_bottom is %d" %table_bottom)
                    
                if (extraction_method[Bank_Name]['Method'] == 'Tabula'):
                    ## Extract Using Tabula's Read Pdf
                    # Add a slight padding at the bottom
                    #print (table_bottom)
                    page_df = tabula.read_pdf(document, pages=actual_page, pandas_options = {'header': None}, guess = False, silent = True, lattice = extraction_method[Bank_Name]['Lattice'], stream = not extraction_method[Bank_Name]['Lattice'], area = [table_top,0,table_bottom,page.width])
                    page_df = page_df.dropna(axis=1,how="all")
                    page_df = page_df.T.reset_index(drop=True).T
                    #print ("I am here inside tabula")
                
                elif (extraction_method[Bank_Name]['Method'] == 'Plumber'):
                
                    ## Extract Using PDF Plumber Extract Table
                    cropped_page = page.crop((0, table_top , page.width, table_bottom))
                    page_table = cropped_page.extract_table(extraction_method[Bank_Name]['table_settings'])
                    page_df = pd.DataFrame(page_table)
                    page_df.replace('\n',' ', regex=True, inplace = True)
                    
                else:
                    print ("Gotta define settings for the %s Bank, it seems" %Bank_Name)
                    pass
            else:
                pass
            
        print (page_df)
        
        ## CLEANING THE DATA ##
        
        #0 If for certain banks, the date & description is coming in the same column, split it
        if (Bank_Name == 'SYNDICATE' or Bank_Name == 'KARNATAKA'):
            regex_date = r"(?:(?:31(\/| |-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/| |-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/| |-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|(?:0?[1-9]|1\d|2[0-8])(\/| |-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"
            to_split_date = page_df[page_df[0].str.contains(regex_date,regex=True)== True]
            dateDf = pd.DataFrame()
            dateDf['Date'] = to_split_date[0].str.split(" ", 1).str[0]
            dateDf['Description'] = to_split_date[0].str.split(" ", 1).str[1]
            newDf_1 = pd.concat([dateDf, to_split_date],axis=1).drop([0],axis=1)
            newDf_2 = page_df[~page_df.index.isin(to_split_date.index)]
            newDf_2['Date'] = np.nan
            newDf_2['Description'] = newDf_2[0]
            newDf = newDf_2.drop([0],axis=1)
            page_df_1 = pd.concat([newDf_1, newDf])
            page_df = page_df_1.sort_index(axis=0)
        
        #1 Assign the header to the page data
        page_df = assign_header(page_df,Bank_Name)
        #print (page_df)

        #2 Combine the rows that may be getting split in multiple rows...
        rolling_group.group = 0 #static variable
        
        groups = page_df.groupby(page_df["Balance"].apply(rolling_group),as_index=False)
        groupFunct = lambda g: pd.Series([joinFunc(g,col) for col in g.columns],index=g.columns)
        pade_df_clean = pd.DataFrame()
        page_df_clean = groups.apply(groupFunct)

        #3 Check if additional column exists and if yes, combine the columns that contain info about Cheque etc with Description

        colNames = page_df_clean.columns[page_df_clean.columns.str.contains(pat = 'Additional Info')]
        if (colNames.tolist() != []):
            page_df_clean['Description'] = page_df_clean[['Description', 'Additional Info']].apply(lambda x: ' '.join(x), axis=1)
            page_df_clean.drop(['Additional Info'], axis=1, inplace = True)

        #4 Check if Useless column exists and if yes, delete it

        colNames = page_df_clean.columns[page_df_clean.columns.str.contains(pat = 'Useless')]
        if (colNames.tolist() != []):
            page_df_clean.drop(['Useless'], axis=1, inplace = True)

        #5 Remove rows where Balance is not a valid entry
    
        page_df_clean = page_df_clean[page_df_clean['Balance'].str.contains('\\d+(\\.\\d{1,2})', regex = True)]
        page_df_1 = pd.DataFrame()
        page_df_1 = page_df_clean.reset_index(drop=True)
        #print (page_df_1)

        #6 Check if Withdrawal / Despoit Column exists, and if yes call the split_cr_dr function to split credit-debit data
        ## This should be done before the Amount (Cr/Dr) check as otherwise Cr/Dr will match and show error

        colNames = page_df_1.columns[page_df_1.columns.str.contains(r'\bWithdrawal\b.*\(Cr|Dr\)', regex=True)]
        #print (colNames.tolist())
        if (colNames.tolist() != []):
            page_df_2 = split_cr_dr(page_df_1)
        else:
            page_df_2 = page_df_1

        #7 Check if Amount & Cr/Dr column are there and if yes, apply the split_amount function
        colNames = page_df_2.columns[page_df_2.columns.str.contains(r'\bDr\b|\bCr\b', regex=True, flags = re.IGNORECASE)]
        #print (colNames.tolist())
        if (colNames.tolist() != []):
            page_df_3 = split_amount(page_df_2)
        else:
            page_df_3 = page_df_2

        #print (page_df_3)

        #8 Fill empty row dates with previous date
        date_df = page_df_3['Date']
        date_df.replace(r'', np.nan, regex=True, inplace = True)
        date_df.fillna(method='ffill', inplace = True)
        page_df_3['Date'] = date_df
        
        #print (page_df_3)
        
        #9 Replace all NaN with empty space
        final_page_df = page_df_3.replace(np.nan, '', regex=True)
        #print (final_page_df)
        
        
        #10 Check if there is no Credit Column, and if so, add an empty column
        colNames = final_page_df.columns[final_page_df.columns.str.contains(r'\bCredit\b', regex=True)]
        #print (colNames.tolist())
        if (colNames.tolist() == []):
            final_page_df["Credit"] = ""
        
        #print (final_page_df)
        
        #11 Create final standardized table
        final_page_data = final_page_df[['Date','Description', 'Credit', 'Debit','Balance']]
        #print (final_page_data)
    
    except:
        pass
    #print (final_page_data)
    master_data = master_data.append(final_page_data, ignore_index = True)


# In[196]:


##7 
master_data


# In[195]:


#master_data['Description'][71]

