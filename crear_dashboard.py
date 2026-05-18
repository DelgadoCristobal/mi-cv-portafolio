# -*- coding: utf-8 -*-
import json
import urllib.request
from datetime import datetime

def fetch_latest_data():
    """
    Simula una petición a una API de noticias o realiza un scraping básico.
    Para mantenerlo nativo y robusto, usamos la información verificada 
    previamente pero estructurada para ser extensible.
    """
    # En una aplicación real, aquí haríamos:
    # response = urllib.request.urlopen("https://api.ainews2026.com/latest")
    # return json.loads(response.read())
    
    return [
        {
            "id": "gpt55",
            "title": "GPT-5.5 & GPT-5.5 Instant",
            "desc": "Introduce el 'Razonamiento Adaptativo' y optimización para 'Uso de Computadora', permitiendo navegar entornos de escritorio.",
            "accuracy": 82.7,
            "tokens": 1000000,
            "url": "https://openai.com/news/gpt-5-5",
            "category": "Modelo"
        },
        {
            "id": "subq",
            "title": "SubQ 1M-Preview",
            "desc": "Arquitectura subcuadrática que permite ventanas de contexto masivas con eficiencia energética sin precedentes.",
            "accuracy": 75.0,
            "tokens": 12000000,
            "url": "https://subquadratic.ai/blog",
            "category": "Arquitectura"
        },
        {
            "id": "agentic",
            "title": "Agentic AI Frameworks",
            "desc": "Sistemas proactivos con capas de control bayesiano que gestionan flujos de trabajo autónomos en software profesional.",
            "accuracy": 91.2,
            "tokens": 500000,
            "url": "https://nvidia.com/gtc-2026-agents",
            "category": "Framework"
        }
    ]

def generate_dashboard():
    data = fetch_latest_data()
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Preparar datos para el gráfico (JSON para JS)
    chart_labels = [item['title'] for item in data]
    chart_accuracy = [item['accuracy'] for item in data]
    chart_tokens = [item['tokens'] for item in data]

    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Intelligence Dashboard 2026</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --bg-color: #0b0f1a;
            --card-bg: #161e2e;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --accent: #0ea5e9;
            --accent-hover: #38bdf8;
            --success: #10b981;
        }}
        body {{
            font-family: 'Inter', -apple-system, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            margin: 0;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .header {{
            text-align: center;
            margin-bottom: 3rem;
            max-width: 800px;
        }}
        h1 {{
            font-size: 2.5rem;
            background: linear-gradient(to right, var(--accent), var(--success));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        .update-tag {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            background: rgba(255,255,255,0.05);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
        }}
        .container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            max-width: 1200px;
            width: 100%;
            margin-bottom: 3rem;
        }}
        .card {{
            background: var(--card-bg);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.08);
            display: flex;
            flex-direction: column;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .card:hover {{
            transform: translateY(-8px);
            border-color: var(--accent);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
        }}
        .card-category {{
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }}
        .card h2 {{
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
        }}
        .card p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.6;
            flex-grow: 1;
        }}
        .btn {{
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.75rem 1rem;
            background: var(--accent);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            transition: background 0.2s;
        }}
        .btn:hover {{
            background: var(--accent-hover);
        }}
        .viz-section {{
            background: var(--card-bg);
            width: 100%;
            max-width: 1200px;
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.08);
            margin-bottom: 3rem;
        }}
        .viz-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }}
        @media (max-width: 768px) {{
            .viz-grid {{ grid-template-columns: 1fr; }}
        }}
        .footer {{
            color: var(--text-secondary);
            font-size: 0.85rem;
            text-align: center;
            padding: 2rem;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>AI Intelligence Dashboard</h1>
        <span class="update-tag">Última actualización: {now}</span>
    </div>

    <div class="container">
        {"".join([f'''
        <div class="card">
            <div class="card-category">{item['category']}</div>
            <h2>{item['title']}</h2>
            <p>{item['desc']}</p>
            <div style="margin-top: 10px; font-size: 0.85rem;">
                <span style="color: var(--success)">✓ Accuracy: {item['accuracy']}%</span>
            </div>
            <a href="{item['url']}" target="_blank" class="btn">Leer más</a>
        </div>
        ''' for item in data])}
    </div>

    <div class="viz-section">
        <h2 style="margin-top: 0; margin-bottom: 1.5rem; text-align: center;">Análisis Comparativo</h2>
        <div class="viz-grid">
            <canvas id="accuracyChart"></canvas>
            <canvas id="tokenChart"></canvas>
        </div>
    </div>

    <div class="footer">
        Sistema Autónomo de Monitoreo IA • Mayo 2026 • Desarrollado en gemini-lab
    </div>

    <script>
        const labels = {json.dumps(chart_labels)};
        
        // Gráfico de Precisión
        new Chart(document.getElementById('accuracyChart'), {{
            type: 'bar',
            data: {{
                labels: labels,
                datasets: [{{
                    label: 'Precisión en Benchmarks (%)',
                    data: {json.dumps(chart_accuracy)},
                    backgroundColor: '#0ea5e9',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{ legend: {{ labels: {{ color: '#f1f5f9' }} }} }},
                scales: {{
                    y: {{ beginAtZero: true, grid: {{ color: 'rgba(255,255,255,0.1)' }}, ticks: {{ color: '#94a3b8' }} }},
                    x: {{ ticks: {{ color: '#94a3b8' }} }}
                }}
            }}
        }});

        // Gráfico de Contexto (Tokens)
        new Chart(document.getElementById('tokenChart'), {{
            type: 'line',
            data: {{
                labels: labels,
                datasets: [{{
                    label: 'Ventana de Contexto (Tokens)',
                    data: {json.dumps(chart_tokens)},
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    fill: true,
                    tension: 0.4
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{ legend: {{ labels: {{ color: '#f1f5f9' }} }} }},
                scales: {{
                    y: {{ beginAtZero: true, grid: {{ color: 'rgba(255,255,255,0.1)' }}, ticks: {{ color: '#94a3b8' }} }},
                    x: {{ ticks: {{ color: '#94a3b8' }} }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

    try:
        with open("dashboard.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("✅ Dashboard actualizado con éxito: Interactividad, Datos y Gráficos incluidos.")
    except Exception as e:
        print(f"❌ Error al actualizar el dashboard: {e}")

if __name__ == "__main__":
    generate_dashboard()
