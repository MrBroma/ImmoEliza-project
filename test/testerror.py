from bs4 import BeautifulSoup

# Exemple de contenu HTML
html_content = '''
<html>
<head><title>Page Title</title></head>
<body>
<h1 class="title--1 page-error__title empty-state__title">Sorry, no matching results.</h1>
</body>
</html>
'''

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Fonction pour vérifier la présence du texte
def check_text_presence(soup):
    error_message_element = soup.find('h1', class_='title--1 page-error__title empty-state__title')
    if error_message_element:
        return 'Sorry, no matching results.' in error_message_element.text
    return False

# Utilisation d'une boucle while pour vérifier la présence du texte
while True:
    if check_text_presence(soup):
        print("Le texte 'Sorry, no matching results.' est présent.")
        break  # Sortir de la boucle si le texte est trouvé
    else:
        print("Le texte 'Sorry, no matching results.' n'est pas présent.")
        # Effectuer d'autres actions ou attendre avant de vérifier à nouveau
