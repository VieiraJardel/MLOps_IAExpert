import os
import logging
from dotenv import load_dotenv

load_dotenv()

if os.getenv("USE_DAGSHUB", "0") == "1":
    import dagshub
    dagshub.init(repo_owner="dennymarcels", repo_name="mlops_project")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)
