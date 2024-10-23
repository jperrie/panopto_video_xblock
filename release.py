import os
import subprocess
import argparse
import shutil
from datetime import datetime

# Function to delete the build and dist folders
def delete_folders():
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Deleted {folder} folder.")

# Function to rebuild the build and dist folders
def rebuild_folders():
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)
    print("Rebuilt build and dist folders.")

# Function to push changes to GitHub
def push_to_github(user, password, message):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push", "https://{}:{}@github.com/jperrie/panopto_video_xblock.git".format(user, password)], check=True)
    print("Pushed changes to GitHub.")

# Function to update Tutor configuration
def update_tutor_config():
    subprocess.run(["tutor", "config", "save", "--remove", "OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/jperrie/panopto_video_xblock.git"], check=True)
    subprocess.run(["tutor", "config", "save", "--append", "OPENEDX_EXTRA_PIP_REQUIREMENTS=git+https://github.com/jperrie/panopto_video_xblock.git"], check=True)
    subprocess.run(["tutor", "images", "build", "openedx"], check=True)
    print("Updated Tutor configuration.")

# Main function
def main():
    parser = argparse.ArgumentParser(description='Manage XBlock GitHub updates and Tutor configuration.')
    parser.add_argument('--user', default='jperrie', help='GitHub username')
    parser.add_argument('--password', default='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', help='GitHub personal access token')
    parser.add_argument('--message', default=f"Update on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", help='Commit message for GitHub')
    parser.add_argument('--no-cache', action='store_true', help='Skip cache during rebuild')

    args = parser.parse_args()

    delete_folders()

    rebuild_folders()

    push_to_github(args.user, args.password, args.message)

    update_tutor_config()

if __name__ == '__main__':
    main()
