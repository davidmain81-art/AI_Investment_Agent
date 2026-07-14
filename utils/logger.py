"""
System Logger
Version 1.0
"""

import logging
import os

LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "investment_agent.log"
)

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

)

logger = logging.getLogger("AI_AGENT")


def log_info(message):

    logger.info(message)


def log_error(message):

    logger.error(message)


def log_warning(message):

    logger.warning(message)