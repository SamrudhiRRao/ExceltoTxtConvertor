import pandas as pd
from tabulate import tabulate

def final_txt(txtcode,txtfile):
    
    final_txtFile = open(txtfile, 'w') # opening the file in write mode
    final_txtFile=final_txtFile.write(txtcode) # write the txtcode onto the final_txtFile