import logging
# logger = logging.getLogger(__name__) # tak zrobimy np. pisząc bibliotekę
logger = logging.getLogger("training.matematyka")

def pierwiastek(x):
    logger.debug("Liczę pierwiastek z %s", x)
    return x ** 0.5
