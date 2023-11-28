import logging
logger = logging.getLogger("training")

import matematyka

def main():
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    formatter = logging.Formatter(fmt="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'", datefmt="%Y-%m-%d %H:%M:%S")
    sh.setFormatter(formatter)

    logger.addHandler(sh)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

    matematyka.pierwiastek(4)

if __name__ == "__main__":
    main()
