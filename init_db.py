import sqlite3

def init_db():
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        classif1_label TEXT,
        sector TEXT,
        year INTEGER,
        obs_value REAL,
        region TEXT
    )''')

    data = [
    ('Broad sector', 'Total', 2023, 2446.943, 'Rabat-Salé-Kenitra'),
    ('Broad sector', 'Total', 2023, 2446.943, 'Rabat-Salé-Kenitra'),
    ('Broad sector', 'Agriculture', 2023, 1161.473, 'Béni Mellal-khénitra'),
    ('Broad sector', 'Industry', 2023, 338.379, 'Béni Mellal-khénitra'),
    ('Broad sector', 'Services', 2023, 947.091, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Total', 2023, 2446.943, 'Casablanca-settat'),
    ('Aggregate', 'Agriculture', 2023, 1161.473, 'Casablanca-settat'),
    ('Aggregate', 'Manufacturing', 2023, 323.557, 'Casablanca-settat'),
    ('Aggregate', 'Construction', 2023, 8.376, 'Marrakech-safi'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2023, 6.446, 'Marrakech-safi'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2023, 353.492, 'Marrakech-safi'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2023, 593.599, 'Drâa-Tafilalet'),
    ('Detailed', 'Total', 2023, 2446.943, 'Drâa-Tafilalet'),
    ('Detailed', 'Agriculture; forestry and fishing ~ISIC rev.4 A', 2023, 1161.473, 'Drâa-Tafilalet'),
    ('Detailed', 'Mining and quarrying ~ISIC rev.4 B', 2023, 2.156, 'Souss-Massa-Draâ'),
    ('Detailed', 'Manufacturing ~ISIC rev.4 C', 2023, 323.557, 'Souss-Massa-Draâ'),
    ('Detailed', 'Utilities ~ISIC rev.4 D; E', 2023, 4.29, 'Souss-Massa-Draâ'),
    ('Detailed', 'Construction ~ISIC rev.4 F', 2023, 8.376, 'Région de Sud'),
    ('Detailed', 'Wholesale and retail trade; repair of motor vehicles and motorcycles ~ISIC rev.4 G', 2023, 210.629, 'Région de Sud'),
    ('Detailed', 'Transport; storage and communication ~ISIC rev.4 H; J', 2023, 15.7, 'Région de Sud'),
    ('Detailed', 'Accommodation and food service activities ~ISIC rev.4 I', 2023, 78.651, 'Ensemble'),
    ('Detailed', 'Financial and insurance activities ~ISIC rev.4 K', 2023, 25.132, 'Ensemble'),
    ('Detailed', 'Real estate; business and administrative activities ~ISIC rev.4 L; M; N', 2023, 23.381, 'Ensemble'),
    ('Detailed', 'Public administration and defence; compulsory social security ~ISIC rev.4 O', 2023, 89.09, 'Tanger-Tetouan-Al Hoceima'),
    ('Detailed', 'Education ~ISIC rev.4 P', 2023, 223.391, 'Tanger-Tetouan-Al Hoceima'),
    ('Detailed', 'Human health and social work activities ~ISIC rev.4 Q', 2023, 101.473, 'Tanger-Tetouan-Al Hoceima'),
    ('Detailed', 'Other services ~ISIC rev.4 R; S; T; U', 2023, 179.644, 'Oriental'),
    ('Broad sector', 'Total', 2022, 2383.035, 'Oriental'),
    ('Broad sector', 'Agriculture', 2022, 1120.784, 'Oriental'),
    ('Broad sector', 'Industry', 2022, 330.765, 'Fès-Méknès'),
    ('Broad sector', 'Services', 2022, 931.486, 'Fès-Méknès'),
    ('Aggregate', 'Total', 2022, 2383.035, 'Fès-Méknès'),
    ('Aggregate', 'Agriculture', 2022, 1120.784, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Manufacturing', 2022, 316.283, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Construction', 2022, 8.213, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2022, 6.269, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2022, 343.952, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2022, 587.534, 'Béni Mellal-khénitra'),
    ('Detailed', 'Total', 2022, 2383.035, 'Casablanca-settat'),
    ('Detailed', 'Agriculture; forestry and fishing ~ISIC rev.4 A', 2022, 1120.784, 'Casablanca-settat'),
    ('Detailed', 'Mining and quarrying ~ISIC rev.4 B', 2022, 2.045, 'Casablanca-settat'),
    ('Detailed', 'Manufacturing ~ISIC rev.4 C', 2022, 316.283, 'Marrakech-safi'),
    ('Detailed', 'Utilities ~ISIC rev.4 D; E', 2022, 4.224, 'Marrakech-safi'),
    ('Detailed', 'Construction ~ISIC rev.4 F', 2022, 8.213, 'Marrakech-safi'),
    ('Detailed', 'Wholesale and retail trade; repair of motor vehicles and motorcycles ~ISIC rev.4 G', 2022, 206.464, 'Drâa-Tafilalet'),
    ('Detailed', 'Transport; storage and communication ~ISIC rev.4 H; J', 2022, 14.195, 'Drâa-Tafilalet'),
    ('Detailed', 'Accommodation and food service activities ~ISIC rev.4 I', 2022, 77.193, 'Drâa-Tafilalet'),
    ('Detailed', 'Financial and insurance activities ~ISIC rev.4 K', 2022, 26.133, 'Souss-Massa-Draâ'),
    ('Detailed', 'Real estate; business and administrative activities ~ISIC rev.4 L; M; N', 2022, 19.967, 'Souss-Massa-Draâ'),
    ('Detailed', 'Public administration and defence; compulsory social security ~ISIC rev.4 O', 2022, 88.526, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Total', 2020, 2567.327, 'Drâa-Tafilalet'),
    ('Aggregate', 'Agriculture', 2020, 1296.753, 'Drâa-Tafilalet'),
    ('Aggregate', 'Industry', 2020, 354.328, 'Drâa-Tafilalet'),
    ('Aggregate', 'Services', 2020, 916.246, 'Ensemble'),
    ('Aggregate', 'Total', 2019, 2567.327, 'Ensemble'),
    ('Aggregate', 'Agriculture', 2019, 1296.753, 'Ensemble'),
    ('Aggregate', 'Manufacturing', 2019, 339.364, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Construction', 2019, 8.697, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2019, 6.266, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2019, 345.101, 'Oriental'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2019, 571.146, 'Oriental'),
    ('Aggregate', 'Total', 2019, 2567.327, 'Oriental'),
    ('Aggregate', 'Agriculture', 2019, 1296.753, 'Fès-Méknès'),
    ('Aggregate', 'Mining and quarrying', 2019, 1.98, 'Fès-Méknès'),
    ('Aggregate', 'Manufacturing', 2019, 339.364, 'Fès-Méknès'),
    ('Aggregate', 'Utilities', 2019, 4.286, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Construction', 2019, 8.697, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Wholesale and retail trade; repair of motor vehicles and motorcycles', 2019, 213.614, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Transport; storage and communication', 2019, 15.174, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Accommodation and food service activities', 2019, 70.071, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Financial and insurance activities', 2019, 25.102, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Real estate; business and administrative activities', 2019, 21.14, 'Casablanca-settat'),
    ('Aggregate', 'Public administration and defence; compulsory social security', 2019, 87.058, 'Casablanca-settat'),
    ('Aggregate', 'Education', 2019, 212.313, 'Casablanca-settat'),
    ('Aggregate', 'Human health and social work activities', 2019, 92.33, 'Marrakech-safi'),
    ('Aggregate', 'Other services', 2019, 179.444, 'Marrakech-safi'),
    ('Aggregate', 'Total', 2018, 2564.023, 'Marrakech-safi'),
    ('Aggregate', 'Agriculture', 2018, 1327.006, 'Drâa-Tafilalet'),
    ('Aggregate', 'Industry', 2018, 349.43, 'Drâa-Tafilalet'),
    ('Aggregate', 'Services', 2018, 887.588, 'Drâa-Tafilalet'),
    ('Aggregate', 'Total', 2018, 2564.023, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Agriculture', 2018, 1327.006, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Manufacturing', 2018, 334.91, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Construction', 2018, 8.411, 'Région de Sud'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2018, 6.109, 'Région de Sud'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2018, 330.623, 'Région de Sud'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2018, 556.964, 'Ensemble'),
    ('Aggregate', 'Total', 2018, 2564.023, 'Ensemble'),
    ('Aggregate', 'Agriculture', 2018, 1327.006, 'Ensemble'),
    ('Aggregate', 'Mining and quarrying', 2018, 1.869, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Manufacturing', 2018, 334.91, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Utilities', 2018, 4.239, 'Tanger-Tetouan-Al Hoceima'),
    ('Aggregate', 'Construction', 2018, 8.411, 'Oriental'),
    ('Aggregate', 'Wholesale and retail trade; repair of motor vehicles and motorcycles', 2018, 205.632, 'Oriental'),
    ('Aggregate', 'Transport; storage and communication', 2018, 14.523, 'Oriental'),
    ('Aggregate', 'Accommodation and food service activities', 2018, 66.295, 'Fès-Méknès'),
    ('Aggregate', 'Financial and insurance activities', 2018, 24.373, 'Fès-Méknès'),
    ('Aggregate', 'Real estate; business and administrative activities', 2018, 19.801, 'Fès-Méknès'),
    ('Aggregate', 'Public administration and defence; compulsory social security', 2018, 85.585, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Education', 2018, 205.836, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Human health and social work activities', 2018, 88.996, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Other services', 2018, 176.547, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Total', 2017, 2561.407, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Agriculture', 2017, 1360.539, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Industry', 2017, 343.228, 'Casablanca-settat'),
    ('Aggregate', 'Services', 2017, 857.639, 'Casablanca-settat'),
    ('Aggregate', 'Total', 2017, 2561.407, 'Casablanca-settat'),
    ('Aggregate', 'Agriculture', 2017, 1360.539, 'Marrakech-safi'),
    ('Aggregate', 'Manufacturing', 2017, 329.185, 'Marrakech-safi'),
    ('Aggregate', 'Construction', 2017, 8.102, 'Marrakech-safi'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2017, 5.941, 'Drâa-Tafilalet'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2017, 315.929, 'Drâa-Tafilalet'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2017, 541.71, 'Drâa-Tafilalet'),
    ('Aggregate', 'Total', 2017, 2561.407, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Agriculture', 2017, 1360.539, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Mining and quarrying', 2017, 1.786, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Manufacturing', 2017, 329.185, 'Région de Sud'),
    ('Aggregate', 'Utilities', 2017, 4.156, 'Région de Sud'),
    ('Aggregate', 'Construction', 2017, 8.102, 'Région de Sud'),
    ('Aggregate', 'Wholesale and retail trade; repair of motor vehicles and motorcycles', 2017, 197.154, 'Ensemble'),
    ('Aggregate', 'Transport; storage and communication', 2017, 13.85, 'Ensemble'),
    ('Aggregate', 'Accommodation and food service activities', 2017, 62.793, 'Ensemble'),
    ('Aggregate', 'Financial and insurance activities', 2017, 23.608, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Real estate; business and administrative activities', 2017, 18.525, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Public administration and defence; compulsory social security', 2017, 83.995, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Education', 2017, 198.787, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Human health and social work activities', 2017, 85.677, 'Casablanca-settat'),
    ('Aggregate', 'Other services', 2017, 173.252, 'Casablanca-settat'),
    ('Aggregate', 'Total', 2016, 2618.78, 'Casablanca-settat'),
    ('Aggregate', 'Agriculture', 2016, 1429.22, 'Marrakech-safi'),
    ('Aggregate', 'Industry', 2016, 343.237, 'Marrakech-safi'),
    ('Aggregate', 'Services', 2016, 846.323, 'Marrakech-safi'),
    ('Aggregate', 'Total', 2016, 2618.78, 'Drâa-Tafilalet'),
    ('Aggregate', 'Agriculture', 2016, 1429.22, 'Drâa-Tafilalet'),
    ('Aggregate', 'Manufacturing', 2016, 329.553, 'Drâa-Tafilalet'),
    ('Aggregate', 'Construction', 2016, 7.915, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2016, 5.945, 'Souss-Massa-Draâ'),
    ('Aggregate', 'Public administration and defence; compulsory social security', 2016, 80.872, 'Région de Sud'),
    ('Aggregate', 'Agriculture', 2013, 1567.181, 'Ensemble'),
    ('Aggregate', 'Industry', 2013, 344.32, 'Ensemble'),
    ('Aggregate', 'Services', 2013, 786.027, 'Ensemble'),
    ('Aggregate', 'Total', 2012, 2600.81, 'Région de Sud'),
    ('Aggregate', 'Agriculture', 2012, 1543.21, 'Région de Sud'),
    ('Aggregate', 'Industry', 2012, 339.78, 'Région de Sud'),
    ('Aggregate', 'Services', 2012, 717.82, 'Région de Sud'),
    ('Detailed', 'Agriculture; forestry and fishing ~ISIC rev.4 A', 2012, 1543.21, 'Région de Sud'),
    ('Detailed', 'Mining and quarrying ~ISIC rev.4 B', 2012, 1.36, 'Région de Sud'),
    ('Detailed', 'Manufacturing ~ISIC rev.4 C', 2012, 329.45, 'Région de Sud'),
    ('Detailed', 'Utilities ~ISIC rev.4 D; E', 2012, 3.57, 'Région de Sud'),
    ('Detailed', 'Construction ~ISIC rev.4 F', 2012, 7.32, 'Région de Sud'),
    ('Detailed', 'Wholesale and retail trade; repair of motor vehicles and motorcycles ~ISIC rev.4 G', 2012, 185.32, 'Région de Sud'),
    ('Detailed', 'Transport; storage and communication ~ISIC rev.4 H; J', 2012, 12.47, 'Région de Sud'),
    ('Detailed', 'Accommodation and food service activities ~ISIC rev.4 I', 2012, 50.89, 'Région de Sud'),
    ('Detailed', 'Financial and insurance activities ~ISIC rev.4 K', 2012, 21.64, 'Région de Sud'),
    ('Detailed', 'Real estate; business and administrative activities ~ISIC rev.4 L; M; N', 2012, 14.85, 'Région de Sud'),
    ('Detailed', 'Public administration and defence; compulsory social security ~ISIC rev.4 O', 2012, 82.47, 'Région de Sud'),
    ('Detailed', 'Education ~ISIC rev.4 P', 2012, 168.92, 'Région de Sud'),
    ('Detailed', 'Human health and social work activities ~ISIC rev.4 Q', 2012, 79.45, 'Région de Sud'),
    ('Detailed', 'Other services ~ISIC rev.4 R; S; T; U', 2012, 160.22, 'Région de Sud'),
    ('Aggregate', 'Total', 2011, 2550.35, 'Région de Sud'),
    ('Aggregate', 'Agriculture', 2011, 1522.68, 'Région de Sud'),
    ('Aggregate', 'Industry', 2011, 335.23, 'Région de Sud'),
    ('Aggregate', 'Services', 2011, 692.41, 'Région de Sud'),
    ('Detailed', 'Human health and social work activities ~ISIC rev.4 Q', 2013, 78.539, 'Ensemble'),
    ('Detailed', 'Other services ~ISIC rev.4 R; S; T; U', 2013, 172.128, 'Ensemble'),
    ('Aggregate', 'Total', 2012, 2592.182, 'Région de Sud'),
    ('Aggregate', 'Agriculture', 2012, 1489.432, 'Ensemble'),
    ('Aggregate', 'Industry', 2012, 345.198, 'Ensemble'),
    ('Aggregate', 'Services', 2012, 757.552, 'Ensemble'),
    ('Aggregate', 'Total', 2012, 2592.182, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Agriculture', 2012, 1489.432, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Manufacturing', 2012, 311.013, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Construction', 2012, 6.859, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2012, 5.032, 'Casablanca-settat'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2012, 263.497, 'Casablanca-settat'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2012, 471.266, 'Casablanca-settat'),
    ('Detailed', 'Total', 2012, 2592.182, 'Marrakech-safi'),
    ('Detailed', 'Agriculture; forestry and fishing ~ISIC rev.4 A', 2012, 1489.432, 'Marrakech-safi'),
    ('Detailed', 'Mining and quarrying ~ISIC rev.4 B', 2012, 1.366, 'Marrakech-safi'),
    ('Detailed', 'Manufacturing ~ISIC rev.4 C', 2012, 311.013, 'Drâa-Tafilalet'),
    ('Detailed', 'Utilities ~ISIC rev.4 D; E', 2012, 3.548, 'Drâa-Tafilalet'),
    ('Detailed', 'Construction ~ISIC rev.4 F', 2012, 6.859, 'Drâa-Tafilalet'),
    ('Detailed', 'Wholesale and retail trade; repair of motor vehicles and motorcycles ~ISIC rev.4 G', 2012, 167.301, 'Souss-Massa-Draâ'),
    ('Detailed', 'Transport; storage and communication ~ISIC rev.4 H; J', 2012, 12.321, 'Souss-Massa-Draâ'),
    ('Detailed', 'Accommodation and food service activities ~ISIC rev.4 I', 2012, 49.675, 'Souss-Massa-Draâ'),
    ('Detailed', 'Financial and insurance activities ~ISIC rev.4 K', 2012, 21.932, 'Région de Sud'),
    ('Detailed', 'Real estate; business and administrative activities ~ISIC rev.4 L; M; N', 2012, 14.315, 'Région de Sud'),
    ('Detailed', 'Public administration and defence; compulsory social security ~ISIC rev.4 O', 2012, 80.573, 'Région de Sud'),
    ('Detailed', 'Education ~ISIC rev.4 P', 2012, 162.548, 'Ensemble'),
    ('Detailed', 'Human health and social work activities ~ISIC rev.4 Q', 2012, 74.342, 'Ensemble'),
    ('Detailed', 'Other services ~ISIC rev.4 R; S; T; U', 2012, 160.918, 'Ensemble'),
    ('Aggregate', 'Total', 2011, 2493.318, 'Région de Sud'),
    ('Aggregate', 'Agriculture', 2011, 1403.542, 'Ensemble'),
    ('Aggregate', 'Industry', 2011, 335.120, 'Ensemble'),
    ('Aggregate', 'Services', 2011, 754.656, 'Ensemble'),
    ('Aggregate', 'Total', 2011, 2493.318, 'Rabat-Salé-Kenitra'),
    ('Aggregate', 'Agriculture', 2011, 1403.542, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Manufacturing', 2011, 299.105, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Construction', 2011, 6.156, 'Béni Mellal-khénitra'),
    ('Aggregate', 'Mining and quarrying; Electricity, gas and water supply', 2011, 4.214, 'Casablanca-settat'),
    ('Aggregate', 'Trade, Transportation, Accommodation and Food, and Business and Administrative Services', 2011, 249.892, 'Casablanca-settat'),
    ('Aggregate', 'Public Administration, Community, Social and other Services and Activities', 2011, 450.514, 'Casablanca-settat'),
    ('Detailed', 'Total', 2011, 2493.318, 'Marrakech-safi'),
    ('Detailed', 'Agriculture; forestry and fishing ~ISIC rev.4 A', 2011, 1403.542, 'Marrakech-safi'),
    ('Detailed', 'Mining and quarrying ~ISIC rev.4 B', 2011, 1.214, 'Marrakech-safi'),
    ('Detailed', 'Manufacturing ~ISIC rev.4 C', 2011, 299.105, 'Drâa-Tafilalet'),
    ('Detailed', 'Utilities ~ISIC rev.4 D; E', 2011, 3.311, 'Drâa-Tafilalet'),
    ('Detailed', 'Construction ~ISIC rev.4 F', 2011, 6.156, 'Drâa-Tafilalet'),
    ('Detailed', 'Wholesale and retail trade; repair of motor vehicles and motorcycles ~ISIC rev.4 G', 2011, 158.992, 'Souss-Massa-Draâ'),
    ('Detailed', 'Transport; storage and communication ~ISIC rev.4 H; J', 2011, 11.623, 'Souss-Massa-Draâ'),
    ('Detailed', 'Accommodation and food service activities ~ISIC rev.4 I', 2011, 46.439, 'Souss-Massa-Draâ'),
    ('Detailed', 'Financial and insurance activities ~ISIC rev.4 K', 2011, 20.157, 'Région de Sud'),
    ('Detailed', 'Real estate; business and administrative activities ~ISIC rev.4 L; M; N', 2011, 13.158, 'Région de Sud'),
    ('Detailed', 'Public administration and defence; compulsory social security ~ISIC rev.4 O', 2011, 77.139, 'Région de Sud'),
    ('Detailed', 'Education ~ISIC rev.4 P', 2011, 152.342, 'Ensemble'),
    ('Detailed', 'Human health and social work activities ~ISIC rev.4 Q', 2011, 71.341, 'Ensemble'),
    ('Detailed', 'Other services ~ISIC rev.4 R; S; T; U', 2011, 149.632, 'Ensemble')
]



    cursor.executemany('''INSERT INTO statistics (classif1_label, sector, year, obs_value, region)
                          VALUES (?, ?, ?, ?, ?)''', data)

    conn.commit()
    conn.close()

def query_data(year=None, region=None, sector=None):
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()

    query = "SELECT classif1_label, sector, year, obs_value FROM statistics WHERE 1=1"
    params = []

    if year:
        query += " AND year = ?"
        params.append(year)

    if region:
        query += " AND region = ?"
        params.append(region)

    if sector:
        query += " AND sector = ?"
        params.append(sector)

    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def display_data(data):
    if not data:
        print("Aucune donnée trouvée pour cette combinaison.")
        return

    print("\nRésultats :")
    print("{:<20} {:<40} {:<10} {:<20}".format("Classification", "Secteur", "Année", "Valeur Observée"))
    print("-" * 90)

    for row in data:
        print("{:<20} {:<40} {:<10} {:<20}".format(row[0], row[1], row[2], row[3]))

def display_regions_and_sectors():
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT region FROM statistics")
    regions = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT sector FROM statistics")
    sectors = [row[0] for row in cursor.fetchall()]

    conn.close()
    return regions, sectors

def display_years():
    conn = sqlite3.connect('statistics.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT year FROM statistics ORDER BY year ASC")
    years = [row[0] for row in cursor.fetchall()]

    conn.close()
    return years

def get_user_input():
    print("Bienvenue! Voici les régions disponibles:")
    regions, sectors = display_regions_and_sectors()

    for i, region in enumerate(regions, start=1):
        print(f"{i}. {region}")

    try:
        region_choice = int(input("\nVeuillez entrer le numéro de la région (1-{}): ".format(len(regions))))
        region = regions[region_choice - 1] if 1 <= region_choice <= len(regions) else None

        # Affichage des années disponibles
        years = display_years()
        print("\nVoici les années disponibles:")
        for i, year in enumerate(years, start=1):
            print(f"{i}. {year}")

        year_choice = int(input("\nVeuillez entrer le numéro de l'année (1-{}): ".format(len(years))))
        year = years[year_choice - 1] if 1 <= year_choice <= len(years) else None

        print("\nVoici les secteurs disponibles:")
        for i, sector in enumerate(sectors, start=1):
            print(f"{i}. {sector}")

        sector_choice = int(input("\nVeuillez entrer le numéro du secteur (1-{}): ".format(len(sectors))))
        sector = sectors[sector_choice - 1] if 1 <= sector_choice <= len(sectors) else None

        data = query_data(year, region, sector)
        display_data(data)
    except (ValueError, IndexError):
        print("Entrée invalide. Veuillez réessayer.")

if __name__ == "__main__":
    init_db()
    get_user_input()
