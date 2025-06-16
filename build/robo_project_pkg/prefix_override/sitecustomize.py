import sys
if sys.prefix == '/opt/homebrew/Caskroom/miniconda/base/envs/ros':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/srijanaraut/Desktop/robo_project/install/robo_project_pkg'
