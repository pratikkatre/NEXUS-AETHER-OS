from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS-AETHER-OS | Global Asset Engine</title>
    <style>
        :root { --gold: #ffd700; --neon: #00f2fe; --bg: #000; }
        body { background: var(--bg); color: #fff; font-family: sans-serif; text-align: center; margin: 0; }
        .header { padding: 40px; border-bottom: 3px solid var(--gold); box-shadow: 0 0 30px var(--gold); }
        .container { max-width: 1000px; margin: auto; padding: 40px 20px; }
        .gold-text { color: var(--gold); text-shadow: 0 0 15px rgba(255, 215, 0, 0.4); letter-spacing: 5px; }
        input { width: 85%; padding: 20px; background: #000; border: 2px solid var(--gold); color: white; font-size: 1.5rem; border-radius: 15px; margin-top: 20px; }
        .btn-launch { width: 90%; padding: 20px; background: var(--gold); color: #000; font-weight: 900; border: none; border-radius: 15px; cursor: pointer; margin-top: 30px; font-size: 1.5rem; text-transform: uppercase; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 50px; }
        .card { background: #111; padding: 25px; border-radius: 20px; border-top: 5px solid var(--neon); text-align: left; }
    </style>
</head>
<body>
    <div class="header"><h1 class="gold-text">🔱 NEXUS-AETHER-OS</h1></div>
    <div class="container">
        <p style="color: #888;">GLOBAL WEALTH ENGINE | OWNER: PRATIK KATRE</p>
        <form method="POST">
            <input type="text" name="idea" placeholder="ENTER GLOBAL SEED CONCEPT" required>
            <button type="submit" class="btn-launch">ACTIVATE WEALTH STREAMS 🚀</button>
        </form>
        {% if idea %}
        <div class="grid">
            <div class="card"><h3>📽️ POND5 GOLD</h3><p>Prompt: Cinematic 8K, {{ idea }}, drone shot, Unreal Engine 5.4.</p></div>
            <div class="card" style="border-top-color: var(--gold);"><h3>🎮 UNITY ASSET</h3><p>Bundle: Modular 8K environment maps for {{ idea }}.</p></div>
            <div class="card" style="border-top-color: #ff00cc;"><h3>🌍 GLOBAL TRAFFIC</h3><p>SEO Hook: "How to dominate {{ idea }} market using AI."</p></div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    idea = None
    if request.method == 'POST':
        idea = request.form.get('idea')
    return render_template_string(HTML_CODE, idea=idea)
  
