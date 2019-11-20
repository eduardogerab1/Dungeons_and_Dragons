import sqlite3
from tkinter import messagebox

def banco_r():
    conn = sqlite3.connect("RacasDeD.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS racas(
    Anão
    Elfo
    Halfling
    Humano
    Draconato
    Gnomo
    Orc
    Meio-Elfo
    Meio-Orc
    Tiefling
    Goblin
    Minotauro
    Aarakocra
    Tartaruga
    Gênio
    Golias
    Aasimar
    Shifter
    Shapeshifter
    Bugbear
    Firbolg
    Hobgoblin
    Kenku
    Kobold
    Lagartixa
    Tritão
    Tabaxi
    Yuan-Ti
    Changeling
    Kalashtar
    Warforged
    Gith
    Centauro
    Loxodon
    Simic Hybrid
    Vedalken
    Locathah
    );
    """)

