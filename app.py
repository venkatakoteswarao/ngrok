from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)

# Store the active tunnel
active_tunnel = None

# Set your ngrok authtoken here
ngrok.set_auth_token("2jrvFhUiOQ1ql4Gdah70GYJzat2_6ho2vTYenHNvG9SqPyn48")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deploy', methods=['POST'])
def deploy():
    global active_tunnel

    # Get the local URL from the user
    local_url = request.form.get('local_url')

    # Check if the local URL is provided
    if not local_url:
        return jsonify({'error': 'Local URL is required'}), 400

    # Stop any active tunnel
    if active_tunnel:
        ngrok.disconnect(active_tunnel.public_url)
        active_tunnel = None

    try:
        # Create a public ngrok tunnel
        active_tunnel = ngrok.connect(local_url)
        return jsonify({'public_url': active_tunnel.public_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop():
    global active_tunnel

    # Stop the active tunnel if any
    if active_tunnel:
        ngrok.disconnect(active_tunnel.public_url)
        active_tunnel = None
    return jsonify({'status': 'Tunnel stopped successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
