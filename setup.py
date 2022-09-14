from setuptools import setup

setup(
    name='DataFrameModel',
    version='0.1.0',
    packages=['test', 'src'],
    url='https://github.com/Marius9595/DataFrameModel.git',
    license='MIT',
    author='mario',
    author_email='mariospmdev@gmail.com',
    description='A wrapper of DataFrames to encapsulate and get explicity for your dataframes',
    install_requires=[
        'pandera',
    ],
)