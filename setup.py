from setuptools import setup, find_packages

setup(
    name='DataXtract',
    version='1.0.0',
    description='Data extraction and analysis system',
    author='Mabilikoe Thoahlane',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'flask>=1.1.2',
        'sqlalchemy>=1.3.19',
        'chart.js>=2.9.4',
        'google-api-python-client>=1.12.1',
        'flask-excel>=0.0.7'
    ],
)
