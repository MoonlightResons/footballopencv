import time
import subprocess

def run_bot():
    while True:
        try:
            subprocess.run(['python', 'main.py'])
        except Exception as e:
            print(f"Bot crashed with error: {e}")
            time.sleep(5)  # Wait for 5 seconds before restarting
        print("Restarting bot...")

if __name__ == "__main__":
    run_bot()
