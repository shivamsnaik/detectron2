# Init the comet API as a global so
## it can be used by all other programs
# ==============================================================================
#
#       global_variables.py - Global variables shared by all modules.
#
# ==============================================================================

# Import comet_ml at the top of your file
from comet_ml import Experiment, ExistingExperiment
import os

COMET_LOGGER = None
COMET_LOGGER_EXPERIMENT_ID = None
def init():
    # Init Comet Logger as Global
    global COMET_LOGGER
    global COMET_LOGGER_EXPERIMENT_ID

    if COMET_LOGGER_EXPERIMENT_ID == None:
        COMET_LOGGER = Experiment(
            api_key=os.environ['COMET_API_KEY'],
            project_name="dynamichead",
            workspace="shivamsnaik",
            auto_output_logging="simple"
        )
        COMET_LOGGER_EXPERIMENT_ID = COMET_LOGGER.get_key()
    else:
        COMET_LOGGER = ExistingExperiment(
            api_key=os.environ['COMET_API_KEY'],
            project_name="dynamichead",
            workspace="shivamsnaik",
            auto_output_logging="simple",
            previous_experiment=COMET_LOGGER_EXPERIMENT_ID
        )