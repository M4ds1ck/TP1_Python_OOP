from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.f = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        self.f.write(f"{datetime.now().isoformat()} - {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self.f.close()

    @classmethod
    def lire(cls):
        with open("journal.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
        for ligne in reversed(lignes):
            print(ligne.strip())
