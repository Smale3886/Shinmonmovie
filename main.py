from flask import Flask, redirect, Response
import requests

app = Flask(__name__)

# --- YOUR CREDENTIALS ---
DNS = "https://dhoomtv.xyz"
USER = "P4B9TB9xR8"
PASS = "humongous2tonight"
# ------------------------

# Standard Player Header to prevent blocking
HEADERS = {
    'User-Agent': 'IPTVSmartersPlayer',
}

@app.route('/play/<stream_id>/index.m3u8')
def play_stream(stream_id):
    """
    Generates a temporary link structure similar to SFVIP.
    """
    # Construct the Xtream Codes link
    # Most providers use the /live/user/pass/id.ts or .m3u8 format
    target_url = f"{DNS}/live/{USER}/{PASS}/{stream_id}.ts"
    
    print(f"[*] Requesting Stream ID: {stream_id}")
    print(f"[*] Redirecting to: {target_url}")
    
    # We use a 302 Redirect so your Video Player (VLC/MX) 
    # takes over the connection directly.
    return redirect(target_url)

@app.route('/list')
def get_list():
    """
    Optional: Hit this endpoint to see if your login is working.
    """
    api_url = f"{DNS}/player_api.php?username={USER}&password={PASS}"
    try:
        r = requests.get(api_url, headers=HEADERS, timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    # Runs on port 8000
    print("Bridge started! Link format: http://127.0.0.1:8000/play/ID/index.m3u8")
    app.run(host='0.0.0.0', port=8000)
