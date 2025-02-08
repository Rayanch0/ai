from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 📌 REMPLACE par ton identifiant et mot de passe 
INSTAGRAM_USERNAME = "ramimarino2020@gmail.com"
INSTAGRAM_PASSWORD = "timeline-of-onepiece"

# 📌 Le compte à scraper (ex: "gdg_algiers")
TARGET_ACCOUNT = "gdg_algiers"

# 🚀 Configurer le navigateur
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Exécute sans affichage (optionnel)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 🔐 **Connexion à Instagram**
def login_instagram():
    print("[INFO] Connexion à Instagram...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    # 🔑 Entrer le nom d’utilisateur et le mot de passe
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    
    username_input.send_keys(INSTAGRAM_USERNAME)
    password_input.send_keys(INSTAGRAM_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(7)  # Attendre la connexion
    print("[INFO] Connexion réussie !")

# 📸 **Scraper les publications**
def scrape_posts():
    print(f"[INFO] Accès au compte Instagram : {TARGET_ACCOUNT}...")

    # 📌 Aller sur la page du compte
    driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
    time.sleep(5)

    # 🌍 Trouver les lignes de publications
    rows = driver.find_elements(By.CLASS_NAME, "x1f01sob")  # Classe identifiée pour chaque ligne
    all_posts = []

    for row in rows:
        posts = row.find_elements(By.CLASS_NAME, "x1n2onr6")  # Classe des publications
        for post in posts:
            try:
                try:
                    image_element = post.find_element(By.TAG_NAME, "img")
                    description = image_element.get_attribute("alt")
                except:
                    description = "aucune description"

                # 📜 **Récupérer la description**
                #description_element = post.find_element(By.CLASS_NAME, "_aagu")
                #description = description_element.text.strip() if description_element else "Aucune description"

                # 🎥 **Récupérer le lien du reel (s'il existe)**
                try:
                    reel_link = post.find_element(By.TAG_NAME, "a").get_attribute("href")
                except:
                    reel_link = "Pas de reel"

                # 🖼️ **Récupérer le lien de l’image**
                try:
                    image_element = post.find_element(By.TAG_NAME, "img")
                    image_url = image_element.get_attribute("src")
                except:
                    image_url = "Pas d image"

                # 📅 **(Optionnel) Récupérer la date de la publication** -> À améliorer selon les balises
                post_data = {
                    "description": description,
                    "reel_link": reel_link,
                    "image_url": image_url
                }
                all_posts.append(post_data)

                print(f"\n🔹 Publication trouvée : {post_data}")

            except Exception as e:
                print(f"[ERREUR] Impossible de récupérer une publication : {e}")

    print("[INFO] Scraping terminé.")
    return all_posts

# 🚀 **Exécution du script**
login_instagram()
posts_data = scrape_posts()
driver.quit()
