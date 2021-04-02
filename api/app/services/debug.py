import debugpy
from loguru import logger


def setup_debug_server():
    """Setup Debugpy Server for debugging containers"""
    try:
        logger.info("Debugpy server starting on port 5678")
        debugpy.listen(("0.0.0.0", 5678))
    except RuntimeError:
        logger.info("Debugpy server already initialized")
