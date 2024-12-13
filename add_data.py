import streamlit as st
import pandas as pd 

def add_data():
    df=pd.read_csv('data.csv')
    #clear hutumika kufuta form akishasubmit form 
    with st.form("form 1",clear_on_submit=True):
        col1,col2=st.columns(2)
        order_date=col1._date_input(label="OrderDate")
        region=col2.selectbox("Region",df["Region"])

        col11,col22=st.columns(2)
        city=col11.selectbox("City",df["City"])
        category=col22.selectbox("Category",df["Category"])
    
        col111,col222,col333=st.columns(3)
        product=col111.selectbox("ProductName",df["Product"])
        quantity=col222.number_input("Quantity")
        unit_price=col333.number_input("UnitPrice")
    
        #Button
        btn=st.form_submit_button("Save Data To Excel", type="primary")

        #form validation

        if btn:
            if order_date=="" or region=="" or city==""or category==""or product==""or quantity==0.00  or unit_price==0.00:
             st.warning("All Fields Are Required")
             return False         
            else:
                #insert data
                df=pd.concat([df,pd.DataFrame.from_records([{ 
              
                    'OrderDate': order_date,
                    'Region':region,
                    'City':city,
                    'Category':category,
                    'Product':product,
                    'Quantity':quantity,
                    'UnitPrice':float(unit_price),
                    'TotalPrice':float(quantity)*float(unit_price),

                }])])

                #handle exceptions
            
         
            try:
                df.to_csv("data.csv",index=False)
                st.success(product+ " Has Been Added Successfully !")
                return True
            
            except:
                st.warning("Unable to Write, Please Close Excel File !!") 
                return False
        #st.experimental_rerun
   