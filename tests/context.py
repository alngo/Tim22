import sys
import os

root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(root_path))

from tim22.tim22 import Tim22  # noqa # pylint: disable=unused-import, wrong-import-position
