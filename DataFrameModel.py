from re import match
from pandas import DataFrame
from pandera import DataFrameSchema

from Errors.errors import *


class DataFrameModel:
    def __init__(self, data: DataFrame):
        schema = DataFrameSchema(self._schema_from_class())
        self._verify_there_are_correct_column_declarations(schema)
        self._check_column_mismatches(data, schema)
        self._data = schema.validate(data)

    def _verify_there_are_correct_column_declarations(self, schema):
        are_not_column_declarations = len(schema.columns) == 0
        if are_not_column_declarations:
            raise NoColumnDeclarationsFound()

    def _check_column_mismatches(self, data, schema):
        mismatch = data.columns.difference(schema.columns)
        if not (len(mismatch) == 0):
           raise ColumnsMismatch(
               f"These columns names are not declared in schema:\n"
               f"{mismatch.tolist()}\n"
           )

    @property
    def data(self):
        return self._data

    @classmethod
    def _schema_from_class(cls):
        schema = {}
        for cls_item, cls_item_data in cls.__dict__.items():
            is_column = match(r"^col_[a-zA-Z]", cls_item)
            if is_column:
                cls._add_to_schema(cls_item, cls_item_data, schema)
        return schema

    @classmethod
    def _add_to_schema(cls, column_declaration, column, schema):
        if column.name is None:
            raise NoColumnNameDeclared(f"{column_declaration} has not a name column declared")
        schema[column.name] = column