import threading
import webbrowser
import time
from app import app

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)

# Start Flask in background
threading.Thread(target=run_flask).start()

# Wait for server
time.sleep(2)

# Open app automatically
webbrowser.open("http://127.0.0.1:5000")

# Keep running
input("VideoGPT running... Press ENTER to exit")
