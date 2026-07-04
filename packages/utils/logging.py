import logging
import sys

FORMAT = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'

def configure_logging(verbosity: int = 2):
    level = [logging.WARNING, logging.INFO, logging.DEBUG][min(verbosity, 2)]
    logging.basicConfig(format=FORMAT, level=level, stream=sys.stdout)
