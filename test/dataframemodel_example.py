from DataFrameModel import DataFrameModel
from pandera import Column


class Example(DataFrameModel):
    col_some_data = Column(name="some_data", dtype=int)
    col_other_data = Column(name="other_data", dtype=bool)


class ExampleWithoutColumnName(DataFrameModel):
    col_data = Column(dtype=int)


class ExampleWithoutColumnDeclaration(DataFrameModel):
    pass

class ExampleWithJustIncorrectCodingColumnDeclarations(DataFrameModel):
    _data = Column(name='data', dtype=int)

class ExampleWithAnIncorrectCodingColumnDeclaration(DataFrameModel):
    column_some_data = Column(name='some_data', dtype=int)
    col_other_data = Column(name='other_data', dtype=int)