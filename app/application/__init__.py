__version__ = "0.1"


import logging


# Set-up root logger:
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)


logging.info(f"successfully imported")
