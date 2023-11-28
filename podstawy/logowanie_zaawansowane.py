import logging
logger = logging.getLogger("training")

import matematyka

def main():
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
    formatter_file = logging.Formatter(fmt="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'")

    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = logging.FileHandler("app.log", encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter_file)
    logger.addHandler(fh)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

    matematyka.pierwiastek(4)

if __name__ == "__main__":
    main()
