import os

# To standardise the parent directory
THIS_FILE = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(THIS_FILE)

DATASETS_DIR = os.path.join(PROJECT_ROOT, 'datasets')
MODELS_DIR = os.path.join(PROJECT_ROOT, 'models')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, 'scripts')
PLOTS_DIR = os.path.join(PROJECT_ROOT, 'plots')

# Output folder's subfolders
MODIFIED_ADVBENCH_PATH = os.path.join(OUTPUT_DIR, 'modified_advbench')
XSTEST_PATH = os.path.join(OUTPUT_DIR, 'xstest')

# Subfolders under Modified Advbench
MA_QWEN_0_5B = os.path.join(MODIFIED_ADVBENCH_PATH, 'qwen_0.5b_instruct')
MA_QWEN_1_5B = os.path.join(MODIFIED_ADVBENCH_PATH, 'qwen_1.5b_instruct')

# Subfolders under XSTest
XST_QWEN_0_5B = os.path.join(XSTEST_PATH, 'qwen_0.5b_instruct')
XST_QWEN_1_5B = os.path.join(XSTEST_PATH, 'qwen_1.5b_instruct')
