import logging
from pathlib import Path

# ==========================================
# Log Directory
# ==========================================

LOG_DIR = Path(
    "logs"
)

LOG_DIR.mkdir(
    exist_ok=True
)

# ==========================================
# Logger Config
# ==========================================

logging.basicConfig(
    filename=LOG_DIR / "rag.log",
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(
    "mongodb_rag"
)