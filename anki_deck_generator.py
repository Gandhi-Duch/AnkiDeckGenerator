import pandas as pd
from genanki import Note, Deck, Model, Package


# Charger le fichier CSV
df = pd.read_csv("Cybersecurity_Deck_Expanded_240.csv")

# Définir le modèle Anki
anki_model = Model(
    1607392319,
    "Basic Cybersecurity Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}",
        },
    ],
)

# Créer le deck Anki
anki_deck = Deck(
    2059400110,
    "Cybersecurity Fundamentals Deck",
)

# Ajouter des notes au deck
for _, row in df.iterrows():
    note = Note(
        model=anki_model,
        fields=[row["Question"], row["Réponse"]],
    )
    anki_deck.add_note(note)

# Exporter le deck en fichier .apkg
Package(anki_deck).write_to_file("Cybersecurity_Fundamentals_expanded_240.apkg")
print("Fichier .apkg créé avec succès.")
