# Init the comet API as a global so
## it can be used by all other programs
# ==============================================================================
#
#       global_variables.py - Global variables shared by all modules.
#
# ==============================================================================

# Import comet_ml at the top of your file
from comet_ml import Experiment
import os

COMET_LOGGER = None

def init():
    # Init Comet Logger as Global
    global COMET_LOGGER

    COMET_LOGGER = Experiment(
        api_key=os.environ['COMET_API_KEY'],
        project_name="dynamichead",
        workspace="shivamsnaik",
        auto_output_logging="simple"
    )