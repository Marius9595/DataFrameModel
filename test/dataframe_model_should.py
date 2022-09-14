import unittest

import pandas as pd
from pandera.errors import SchemaError

from Errors.errors import *
from test.dataframemodel_example import *


class DataframeModelShould(unittest.TestCase):
    def test_not_allow_wrap_data_that_does_not_follow_schema(self):
        with self.assertRaises(SchemaError):
            Example(pd.DataFrame([{'some_data': True, 'other_data': 1}]))

    def test_detect_columns_that_does_not_belong_to_schema(self):
        column_mistake = 'other_data_'
        with self.assertRaises(ColumnsMismatch) as context:
            Example(pd.DataFrame([{'some_data': 1, column_mistake: False, 'other_data': False}]))
            self.assertTrue(column_mistake in str(context.exception))

    def test_detect_missing_columns(self):
        with self.assertRaises(SchemaError) as context:
            Example(pd.DataFrame([{'some_data': 1}]))

        missing_column = 'other_data'
        self.assertTrue(missing_column in str(context.exception))

    def test_force_to_declare_column_name(self):
        with self.assertRaises(NoColumnNameDeclared) as context:
            ExampleWithoutColumnName(pd.DataFrame([{'data': 1}]))

        column_declaration = 'col_data'
        self.assertTrue(column_declaration in str(context.exception))

    def test_have_column_declarations(self):
        with self.assertRaises(NoColumnDeclarationsFound) as context:
            ExampleWithoutColumnDeclaration(pd.DataFrame([{'data': 1}]))

    def test_use_prefix_coding_to_declare_columns_to_schema(self):
        with self.assertRaises(NoColumnDeclarationsFound) as context:
            ExampleWithJustIncorrectCodingColumnDeclarations(pd.DataFrame([{'data': 1}]))

    def test_ignore_column_declarations_without_unprefixed_coding(self):
        incorrect_dataframe = pd.DataFrame([{'other_data': 1}])

        dataframeWrapped = ExampleWithAnIncorrectCodingColumnDeclaration(incorrect_dataframe)

        self.assertEqual(incorrect_dataframe.columns, dataframeWrapped.data.columns)



if __name__ == '__main__':
    unittest.main()