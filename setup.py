from setuptools import setup

setup(
    name='DataFrameModel',
    version='0.1.0',
    packages=['DataFrameModel', 'Errors'],
    url='https://github.com/Marius9595/DataFrameModel.git',
    license='MIT',
    author='mario',
    author_email='mariospmdev@gmail.com',
    description='an wrapper to type dataframes',
    install_requires=[
        'pandera',
    ],
)