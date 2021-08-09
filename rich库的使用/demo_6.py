import os
import sys

from rich import print
from rich.columns import Columns

directory = os.listdir(sys.path())
print(Columns(directory))