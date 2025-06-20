# Búsqueda de nombre en redes sociales
nombre = input("🔎 Ingresa un nombre de usuario o alias: ").strip()
plataformas = {
    "Instagram": f"https://www.instagram.com/{nombre}",
    "Twitter": f"https://twitter.com/{nombre}",
    "LinkedIn": f"https://www.linkedin.com/in/{nombre}",
    "Facebook": f"https://www.facebook.com/{nombre}",
}
print("\n🌐 Resultados encontrados:")
for red, url in plataformas.items():
    print(f"🔗 {red}: {url}")
