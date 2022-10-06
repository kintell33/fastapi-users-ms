import os
import importlib
import platform

replace_bars = "\\" if platform.system() == "Windows" else "/"
actual_package = os.path.dirname(__file__).replace(os.getcwd()+replace_bars,"").replace("." + replace_bars + "src" + replace_bars,"src.")
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    importlib.import_module("{}.{}".format(actual_package.replace('/','.'), module[:-3]))
del module 