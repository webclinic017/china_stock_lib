import os
import shutil

import get_data

def test_get_data():
    get_data.get_module_1('survivorship_free')
    assert os.path.isdir("survivorship_free")
    shutil.rmtree("survivorship_free")
    os.remove("survivorship_free.zip")