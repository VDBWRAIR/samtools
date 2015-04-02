from __future__ import absolute_import
from os.path import *
import os
import sys
try:
   from io import StringIO
except ImportError:
   from cStringIO import StringIO


PY3 = sys.version_info[0] == 3
if PY3:
    builtins_name = "builtins"
    import _io
    file = _io.TextIOWrapper
else:
    builtins_name = "__builtin__"

import tempfile
import shutil
from glob import glob
import subprocess
import shlex
import re

from mock import Mock, MagicMock, patch, mock_open, call
from nose.tools import *
from nose.plugins.attrib import attr

from Bio import SeqIO

from . import common
from .common import *
from . import fixtures
from .fixtures import THIS
from . import tdir
