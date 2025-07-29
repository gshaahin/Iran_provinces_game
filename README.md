# 🇮🇷 Iran's Provinces Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

🎮 **Test your knowledge of Iran's geography!**

This is a simple educational game built with Python's Turtle graphics, where you guess the names of Iran's 31 provinces. The game displays a map of Iran, and as you correctly guess each province, its name appears on the map at the correct location.

---

## ✨ Features

- 🗺️ Interactive guessing game for all 31 provinces of Iran
- 🤖 Fuzzy matching for province names (handles typos and close matches)
- 🖼️ Visual feedback using a map of Iran

---

## 🛠️ Requirements

- Python 3.x
- [turtle](https://docs.python.org/3/library/turtle.html) (usually included with Python)
- [pandas](https://pandas.pydata.org/)
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
- [python-Levenshtein](https://pypi.org/project/python-Levenshtein/) (optional, for faster fuzzywuzzy)

---

## 🕹️ How to Play

1. Run `main.py`:
   ```bash
   python main.py
   ```
2. A map of Iran will appear.
3. Enter the name of a province in the prompt. (Fuzzy matching helps with minor typos!)
4. Correct guesses will be displayed on the map.
5. Try to guess all 31 provinces!

---

## 📁 Files

- `main.py` — Main game logic
- `Docs/31_provinces.csv` — Province names and coordinates
- `Docs/Iran.gif` — Map image used in the game

---

## 👤 Credits

Created by **Shahin Gholoubi** 
