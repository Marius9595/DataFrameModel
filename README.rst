DataFrameModel
===========

It is an approach to: 

1) Gain expresivity, explicity and taking advantage of hints 
2) Encapsulate operations and columns references

This approach uses `Pandera <https://pandera.readthedocs.io/en/stable/>`_ , an Extension of Pandas Ecosystem to validate Dataframes. The DataFrameSchema is the element used to build DataFrameModel and Column() to declarate name and typing of each column of the dataframe that will be wrapped. As convention, each column declaration have to start with 'col_'. This one has not to match with name of column, but it is easier to handle encapsulated logic in class if these have the similar names.
 
* Implementation example::

       Class CompanySales(DataFrameModel):
           col_department_1 = Column(name='department one', dtype=float)
           col_department_2 = Column(name='department one, dtype=float)
            
           def total_sales_of_company(self) -> pd.Series:
                return self._data[col_department_1.name, department_2.name].sum(axis=1)
               
As you can see, one operation for bussiness is now encapsulated with dataframe that has all data need to resolved. In other words, dataframe follows the principle *"Tell, don't Ask"*. However, you can still operate with data outside althogh, no the diferrence is: The column names are declared just in one Class and you can access everywhere, also when these are changed, all is affected  

::

        >> CompanySales.col_department_1.name
        >> 'department one'
           
            
            
