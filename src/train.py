import spacy
import random
from spacy.training.example import Example
import os

os.makedirs("model", exist_ok=True)


TRAIN_DATA = [
    ("Amul Milk 500 ml", {"entities": [(0, 9, "PRODUCT")]}),
    ("Amul Milk 1 L", {"entities": [(0, 9, "PRODUCT")]}),

    ("Amul Raw Milk 1 L", {"entities": [(0, 14, "PRODUCT")]}),
    ("Amul Almond Milk 200 ml", {"entities": [(0, 17, "PRODUCT")]}),
    ("Amul Soy Milk 500 ml", {"entities": [(0, 13, "PRODUCT")]}),
    ("Amul Full Cream Milk 1 L", {"entities": [(0, 20, "PRODUCT")]}),

    ("Amul Taza Milk 500 ml", {"entities": [(0, 14, "PRODUCT")]}),
    ("Amul Taza Milk 1 L", {"entities": [(0, 14, "PRODUCT")]}),
    ("Amul Taza Milk 2 L", {"entities": [(0, 14, "PRODUCT")]}),

    ("Amul Butter 100 gm", {"entities": [(0, 11, "PRODUCT")]}),
    ("Amul Butter Salted 200 gm", {"entities": [(0, 19, "PRODUCT")]}),
    ("Amul Butter Unsalted 100 gm", {"entities": [(0, 21, "PRODUCT")]}),
]

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")
ner.add_label("PRODUCT")

optimizer = nlp.begin_training()

for epoch in range(30):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.3, losses=losses)

    print(f"Epoch {epoch+1:02d} | Loss: {losses}")

nlp.to_disk("model/amul_sku_model")
print("✅ Model trained and saved")
