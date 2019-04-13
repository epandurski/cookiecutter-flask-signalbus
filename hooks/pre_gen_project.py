import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{cookiecutter.app_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print(
        'ERROR: The app slug (%s) is not a valid Python module name.' % module_name
    )
    sys.exit(1)
