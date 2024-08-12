from test_package.test import main_report
from test_package.subpackage.subpackage import sub_report

# folder is treated as a module. module plus script py file can serve as a module
# need to add init file to tell python that is a package

main_report()

sub_report()
