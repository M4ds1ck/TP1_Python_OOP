from article import Article

a1 = Article("A01", "Clavier", 150, 10)
a2 = Article("A02", "Souris", 80, 25)
a3 = Article("A03", "Ecran", 1200, 5)

articles = [a1, a2, a3]

for article in articles:
    print(article)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")
