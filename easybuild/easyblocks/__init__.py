import os
from pkgutil import extend_path

# Extend path so python finds our easyblocks in the subdirectories where they are located
subdirs = [chr(l) for l in range(ord('a'), ord('z') + 1)] + ['0']
__path__.extend([os.path.join(__path__[0], subdir) for subdir in subdirs])
