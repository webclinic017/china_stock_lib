## china_stock_data
 china stock data from wind

#  Building wheel for get_data (setup.py)
! pip install --upgrade -q git+https://github.com/jinyiabc/china_stock_data.git

#  Downloaded module data.
import get_data
get_data.get_module_1('survivorship_free')

#  create a Path object for the directory 
import pathlib
data = pathlib.Path('survivorship_free')
