from setuptools import setup

setup(
    name = 'stock_data',
    version = '0.0.4',
    author = 'Alex JIN YI',
    author_email = 'jinyiabc@gmail.com',
    url = 'https://github.com/jinyiabc/china_stock_lib.git',
    py_modules = ['get_data', 'wind'],
    description = 'install data in jupyter notebook',
    install_requires = ['backtrader'],
)

# pip setup.py install