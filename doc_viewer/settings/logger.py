import logging

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[95m', # Magenta
    }
    WHITE = '\033[97m'
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        # Format only the levelname and name with color, message in white
        formatted = f"{color}[{record.levelname}] {record.filename}:{self.RESET} {self.WHITE}{record.getMessage()}{self.RESET}"
        return formatted

def setup_logger(level=logging.DEBUG):
    """Setup the main logger once for the whole project."""
    logger = logging.getLogger()
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(level)
        formatter = ColorFormatter('[%(levelname)s] %(filename)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
