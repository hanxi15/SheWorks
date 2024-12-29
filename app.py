from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connexion à la base de données SQLite pour récupérer les statistiques
def get_statistics(region=None, year=None):
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()
    
    # Requête SQL pour récupérer uniquement les colonnes nécessaires
    query = "SELECT classif1_label, sector, year, obs_value FROM statistics WHERE 1=1"
    params = []
    
    if region and region != 'all':
        query += " AND region = ?"
        params.append(region)
    
    if year:
        query += " AND year = ?"
        params.append(year)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    return rows

# Fonction pour récupérer les régions disponibles depuis la base de données
def get_regions():
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT region FROM statistics")
    regions = cursor.fetchall()
    conn.close()
    return [region[0] for region in regions]

# Fonction pour récupérer les années disponibles depuis la base de données
def get_years():
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT year FROM statistics ORDER BY year ASC")
    years = cursor.fetchall()
    conn.close()
    return [year[0] for year in years]

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Route pour la page de feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback_text = request.form.get('feedback')
        # Enregistrer le feedback dans un fichier
        with open('feedbacks.txt', 'a') as f:
            f.write(feedback_text + '\n')
        return render_template('feedback.html', message="Merci pour votre feedback!")
    return render_template('feedback.html')

# Route pour la page des statistiques
@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    # Récupérer les critères de filtrage (région et année)
    region = request.form.get('region') if request.method == 'POST' else 'all'
    year = request.form.get('year') if request.method == 'POST' else None

    # Récupérer les statistiques filtrées en fonction des critères
    stats = get_statistics(region, year)

    # Récupérer les régions et les années disponibles pour le filtre
    regions = get_regions()
    years = get_years()

    # Passez les valeurs de filtre et les statistiques au template pour l'affichage
    return render_template('statistics.html', stats=stats, selected_region=region, selected_year=year, regions=regions, years=years)

if __name__ == '__main__':
    app.run(debug=True)
