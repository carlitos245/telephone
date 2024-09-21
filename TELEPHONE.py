import psutil
import time
import threading
import os

# Ensemble des applications interdites
forbidden_apps = {"chrome.exe", "firefox.exe", "tiktok.exe", "Instagram.exe", "Facebook.exe"}  # Utilisez les noms de processus réels

# Ensemble des numéros de téléphone interdits
forbidden_numbers = {"+33987654321", "+33111223344"}  # Ajoutez ici les numéros que vous souhaitez bloquer

# Fonction pour vérifier les processus en cours
def check_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in forbidden_apps:
                print(f"Application interdite détectée : {proc.info['name']}")
                proc.terminate()  # Terminer le processus
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Erreur lors de la terminaison du processus : {e}")

# Fonction pour vérifier les appels sortants
def check_calls():
    # Simuler la vérification des appels sortants
    # Remplacez cette partie par l'intégration avec une API de téléphonie réelle
    outgoing_calls = ["+33123456789", "+33111222333"]  # Exemple de numéros appelés
    for number in outgoing_calls:
        if number in forbidden_numbers:
            print(f"Appel interdit détecté vers : {number}")
            # Ajouter le code pour bloquer l'appel ici

# Nouvelle fonction pour désactiver Internet
def disable_internet():
    # Commande pour désactiver l'interface réseau sur Windows
    os.system("netsh interface set interface 'Wi-Fi' admin=disable")
    # Pour Linux, utilisez : os.system("nmcli networking off")
    print("Internet désactivé")

# Fonction principale
def main():
    while True:
        process_thread = threading.Thread(target=check_processes)
        call_thread = threading.Thread(target=check_calls)
        internet_thread = threading.Thread(target=disable_internet)
        
        process_thread.start()
        call_thread.start()
        internet_thread.start()
        
        process_thread.join()
        call_thread.join()
        internet_thread.join()
        
        time.sleep(10)  # Vérifier toutes les 10 secondes

if __name__ == "__main__":
    main()
