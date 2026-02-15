import logging

# Configure the logger once
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create the logger object
logger = logging.getLogger("lurking_with_agent")

# Now, in any other file, just do: 
# from logger import logger