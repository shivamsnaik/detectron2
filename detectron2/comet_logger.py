# Init the comet API as a global so
## it can be used by all other programs
# ==============================================================================
#
#       global_variables.py - Global variables shared by all modules.
#
# ==============================================================================

# Import comet_ml at the top of your file
import comet_ml
import os

COMET_LOGGER = None

def init():
    # Init Comet Logger as Global
    global COMET_LOGGER

    # Check to see if there is a key in environment:
    EXPERIMENT_KEY = os.environ.get("COMET_EXPERIMENT_KEY", None)

    # First, let's see if we continue or start fresh:
    CONTINUE_RUN = False
    if (EXPERIMENT_KEY is not None):
        # There is one, but the experiment might not exist yet:
        api = comet_ml.API() # Assumes API key is set in config/env
        try:
            api_experiment = api.get_experiment_by_key(EXPERIMENT_KEY)
        except Exception:
            api_experiment = None
        if api_experiment is not None:
            CONTINUE_RUN = True

    if CONTINUE_RUN:
        # 1. Recreate the state of ML system before creating experiment
        # otherwise it could try to log params, graph, etc. again
        # ...
        # 2. Setup the existing experiment to carry on:
        experiment = comet_ml.ExistingExperiment(
            api_key=os.environ['COMET_API_KEY'],
            project_name="dynamichead",
            workspace="shivamsnaik",
            auto_output_logging="simple",
            previous_experiment=EXPERIMENT_KEY,
        )

    else:
        # 1. Create the experiment first
        #    This will use the COMET_EXPERIMENT_KEY if defined in env.
        #    Otherwise, you could manually set it here. If you don't
        #    set COMET_EXPERIMENT_KEY, the experiment will get a
        #    random key!
        experiment = comet_ml.Experiment(
            api_key=os.environ['COMET_API_KEY'],
            project_name="dynamichead",
            workspace="shivamsnaik",
            auto_output_logging="simple",
            experiment_key=EXPERIMENT_KEY
        )
        
        # 2. Setup the state of the ML system
        # ...
    COMET_LOGGER = experiment

