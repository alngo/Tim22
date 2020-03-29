import sys
import os

root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(root_path))

import tim22  # noqa # pylint: disable=unused-import, wrong-import-position
