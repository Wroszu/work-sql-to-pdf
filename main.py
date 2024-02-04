import sqlite3
import pandas as pd
import numpy as np
import datetime
from reportlab.platypus import Frame, PageTemplate, BaseDocTemplate, Table, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape

dt = datetime.datetime.now()

def on_page(canvas, doc, pagesize=A4):
    page_num = canvas.getPageNumber()
    canvas.drawString(20, 20, dt.strftime("%d/%m/%Y  %H:%M:%S"))
    canvas.drawCentredString(pagesize[0]/2, 20, str(page_num))
    canvas.drawImage('/home/wroszu/GitHub/work-sql-to-pdf/see-more-sprite.png', 10, 740)

def df2table(df):
    return Table(
      [[Paragraph(col) for col in df.columns]] + df.values.tolist(), 
      style=[
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('LINEBELOW',(0,0), (-1,0), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.lightgrey, colors.white])],
      hAlign = 'LEFT')

conn = sqlite3.connect('/home/wroszu/GitHub/work-sql-to-pdf/sql_files/sqlite-sakila.db')

cursor = conn.cursor()

"""
FROM .sql file:
payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date,last_update)
;
rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update)
;
customer (customer_id,store_id,first_name,last_name,email,address_id,active,create_date,last_update)
;
film_category (film_id,category_id,last_update)
;
film_actor (actor_id,film_id,last_update)
;
inventory (inventory_id,film_id,store_id,last_update)
;
film (film_id,title,description,release_year,language_id,original_language_id,rental_duration,rental_rate,length,replacement_cost,rating,special_features,last_update)
;
category (category_id,name,last_update)
;
store (store_id,manager_staff_id,address_id,last_update)
;
actor (actor_id,first_name,last_name,last_update)
;
city (city_id,city,country_id,last_update)
;
country (country_id,country,last_update)
;
language (language_id,name,last_update)
"""

Tables_list = ['payment', 
               'rental', 
               'customer', 
               'film_category', 
               'film_actor', 
               'inventory', 
               'film', 
               'category', 
               'store', 
               'actor', 
               'city', 
               'country', 
               'language']
Raw_categories_list = ['payment_id,customer_id,staff_id,rental_id,amount,payment_date,last_update',
                'rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update', 
                'customer_id,store_id,first_name,last_name,email,address_id,active,create_date,last_update', 
                'film_id,category_id,last_update', 
                'actor_id,film_id,last_update', 
                'inventory_id,film_id,store_id,last_update', 
                'film_id,title,description,release_year,language_id,original_language_id,rental_duration,rental_rate,length,replacement_cost,rating,special_features,last_update', 
                'category_id,name,last_update', 
                'store_id,manager_staff_id,address_id,last_update', 
                'actor_id,first_name,last_name,last_update', 
                'city_id,city,country_id,last_update', 
                'country_id,country,last_update', 
                'language_id,name,last_update']

Categories_list = []

for table_categories in Raw_categories_list:
    temp = table_categories.split(',')
    Categories_list.append(temp)

Table_number = int(input("Enter number of table You want to export to PDF file:"))

cursor.execute("SELECT * FROM "+str(Tables_list[Table_number]))
rows = cursor.fetchall()

temp_data_list = []
for row in rows:
    row = str(row).replace('(', '')
    row = row.replace(')', '')
    temp = row.split(',')
    temp_data_list.append(temp)

conn.close()

df = pd.DataFrame(np.array(temp_data_list), columns=Categories_list[Table_number])

padding = dict(leftPadding = 20, rightPadding = 20, topPadding = 72, bottomPadding = 40)

portrait_frame = Frame (0, 0, *A4, **padding)
landscape_frame = Frame (0, 0, *landscape(A4), **padding)

portrait_template = PageTemplate(id='portrait', frames=portrait_frame,onPage=on_page, pagesize=A4)

PDF_file_name = str(input("Enter PDF file name (DO NOT USE SPACES!):"))

doc = BaseDocTemplate(PDF_file_name+'.pdf', pageTemplates=portrait_template)

doc.build([df2table(df)])