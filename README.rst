
.. figure:: assets/logo.png
  :align: center
  :scale: 50%
  :alt: DataFrameModel

  
What is DataFrameModel?
---------

It is an approach to: 

1) Gain in expressiveness, explicitness and take advantage of python hints.
2) Encapsulate recurring operations
3) Centralize column names to gain consistency in accessing data
4) Validate easily data

In concrete, it consists in a class wrapper of DataFrames. This one is passed by contructor that validate the contract with column declarations.


This approach uses `Pandera <https://pandera.readthedocs.io/en/stable/>`_ ,
an Extension of Pandas' Ecosystem to validate Dataframes as core.
The DataFrameSchema is the element used to build DataFrameModel
and Column class to declare name and typing of each column of the
dataframe that will be wrapped. I decided as convention, each column
declaration have to start with 'col_'. This one has not to
match with name of column, but it is easier to handle encapsulated
logic in class if these have the similar names (maybe, it will have to match in future improvements).

* Implementation example::

       from DataFrameModel.dataframe_model import DataFrameModel
       from pandera import Column

       class CompanySales(DataFrameModel):
           col_department_1 = Column(name='department one', dtype=float)
           col_department_2 = Column(name='department one, dtype=float)
            
           def total_sales_of_company(self) -> pd.Series:
                return self.data[
                self.col_department_1.name, self.department_2.name
                ].sum(axis=1)
               
As it can be seen, one operation for business is now encapsulated
within dataframe that has all data need to resolved relevant
calculations. In other words, dataframe follows the principle
*"Tell, don't Ask"*. However, you can still operate with data
outside. Although, there is a big difference: The column names
are declared just in one site and you can access everywhere,
also when these are changed, all is affected directly.

::

            >> CompanySales.col_department_1.name
            >> 'department one'


On the other hand, this classes allows you to declare functions that will be
like shortcuts to access a subdataframe more easily and more robust
along your code:

::


           from DataFrameModel.dataframe_model import DataFrameModel
           from pandera import Column
           from pandera.typing import DateTime

           class TenerifeElectricSystem(DataFrameModel):
               col_date = Column(name='date', dtype=DateTime)
               col_diesel_motor = Column(name='diesel motor', dtype=float)
               col_gas_turbines = Column(name='gas turbines', dtype=float)
               col_wind_turbines = Column(name='wind turbines', dtype=float)
               col_combined_cycle = Column(name='combined cycle', dtype=float)
               col_vapor = Column(name='vapor', dtype=float)
               col_photovoltaic = Column(name='photovoltaic', dtype=float)
               col_hydro = Column(name='hydro', dtype=float)

               def renewables(self) -> List[str]:
                    return [
                        self.col_wind_turbines.name, self.col_photovoltaic.name
                    ]
               def conventionals(self) -> List[str]:
                    return [
                        self.col_diesel_motor.name, self.col_gas_turbines.name,
                        self.col_combined_cycle.name, self.col_vapor.name,
                    ]
               def zero_emissions_technologies(self) -> List[str]:
                    return [
                        self.col_wind_turbines.name, self.col_photovoltaic.name,
                        self.col_hydro.name
                    ]

* Usage example::

       >> data = pd.DataFrame(some_today_data_from_tenerife)
       >> tenerife = TenerifeElectricSystem(data)
       >> renewables_today_production = tenerife.data[tenerife.renewables].sum()
       


This last example is the core of motivation to develop DataFrameModel
because this gives to data manipulation consistency and adds semantic.

In addition, Pandera provides `Checkers <https://pandera.readthedocs.io/en/stable/checks.html>`_
for each column to gain integrity.  It can be interesting in ETLs processes when all transformations
were done and you would like a quality data. This consists in functions written by self or it can be used the pre-built checkings of pandera.
Examples from its documentation are ilustratives.

Testing
------

I wrote tests in order to cover the DataFrameModel behaviour as I think it should work
at same time these express the specifications of DataFrameModel. 
I would be grateful for reciving feedback if some cases are not covered

A Real example of its use
--------------------
`DataFramodelUseCaseExample <https://github.com/Marius9595/DataFrameModelUseCaseExample/tree/master>`_

Installation
---------

    ::
      
       > pip install git+https://github.com/Marius9595/DataFrameModel.git
    
