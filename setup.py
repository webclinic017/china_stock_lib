from setuptools import setup

setup(
    name = 'stock_data',
    version = '0.0.6',
    author = 'Alex JIN YI',
    author_email = 'jinyiabc@gmail.com',
    url = 'https://github.com/jinyiabc/china_stock_lib.git',
    py_modules = ['get_data', 'wind', 'data_prep', 'help'],
    description = 'install data in jupyter notebook',
    install_requires = ['backtrader'],
)

# pip  install setup.py
"""
Then, you need a builder, such as PyPA build which you can obtain via pip install build. After downloading it, invoke the builder:
python -m build
"""