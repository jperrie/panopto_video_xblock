import os
import subprocess
import argparse
import shutil
from datetime import datetime

# Function to update Tutor configuration
def update_tutor_config():
    subprocess.run(["tutor", "config", "save", "--remove", "OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/jperrie/panopto_video_xblock.git"], check=True)
    subprocess.run(["tutor", "config", "save", "--append", "OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/jperrie/panopto_video_xblock.git"], check=True)
    #subprocess.run(["tutor", "images", "build", "openedx"], check=True)
    print("Updated Tutor configuration.")
    print("Rebuild the image.")

# Main function
def main():

    update_tutor_config()

if __name__ == '__main__':
    main()
