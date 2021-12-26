import os
import shutil

import get_data
from wind import read_wind_excel


def test_get_data():
    get_data.get_module_1('survivorship_free')
    assert os.path.isdir("survivorship_free")
    shutil.rmtree("survivorship_free")
    os.remove("survivorship_free.zip")

def test_read_wind_excel():
    dir = os.path.join('.','../quant/_notebooks')
    df = read_wind_excel(f'{dir}/csi300.xlsx', '2015-6-18', '2018-6-18')
    pass