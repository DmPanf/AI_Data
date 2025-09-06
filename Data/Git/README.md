# 🧠 FaceScan3 HUD Animation

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/b039970b-62f9-4c33-8f66-44341f6215e3" />


---

## ✨ About the Project
This project experiments with **futuristic face-scanning HUD overlays** 🕹️, combining:
- 🔳 **Corner markers** and **ticks** aligned around the head  
- 🌬️ A **breathing frame effect**, creating a dynamic sci-fi interface feel  
- 🎨 Transparent background support for compositing  
- ⚡ Customizable colors, thickness, and scan animation  

Inspired by modern **AI vision systems** and **face recognition HUDs** from sci-fi movies.  

---

## 🚀 Features
- 🟣 **Dark-violet corners & ticks** with central ticks extending inwards  
- 💨 **Breathing frame animation** — the bounding box smoothly expands/contracts  
- 🔲 **3 ticks per side**, dividing edges into quarters  
- 🖼️ Works with **transparent GIFs**  
- 🎛️ Easy to tweak size, speed, and color

---

## 🛠️ Tech Stack
- [Python 3](https://www.python.org/)  
- [Pillow (PIL)](https://python-pillow.org/)  

---

## 📂 Project Structure
```

.
├── facescan3.gif                   # Original rotating head wireframe
├── facescan3\_overlay\_breathing\_center.gif   # Final result with HUD overlay
├── hud\_overlay.py                  # Python script to add corners, ticks & breathing
└── README.md

````

---

## ⚙️ How to Run
1. Install dependencies:
   ```bash
   pip install pillow
````

2. Run the overlay script:

   ```bash
   python hud_overlay.py
   ```
3. Check the output:

   * `facescan3_overlay_breathing_center.gif` → animated HUD overlay

---

## 🎨 Customization

* Change **color** (RGBA):

  ```python
  color = (90, 0, 140, 255)   # dark violet
  ```
* Adjust **breathing amplitude & speed**:

  ```python
  pulse = int(12 * math.sin(i * 0.2))  # amplitude=12, speed=0.2
  ```
* Resize **corners** and **ticks**:

  ```python
  corner_len = 60
  tick_len = 20
  ```

---

## 📸 Preview

Here’s what the **breathing HUD overlay** looks like in action:

![Preview](facescan3_overlay_breathing_center.gif)

---

## 🤝 Contributing

Feel free to fork the repo, play with colors, or extend the effect with:

* 🌈 Neon glow filters
* 📡 Moving scan lines
* 🔵 Dynamic particle effects

---

## 📬 Contact

👤 **Dmitrii Panfilov**
🔗 [LinkedIn](https://linkedin.com/in/dmpanf) · [Telegram Channel](https://t.me/isai_digital) · [Teletype](https://teletype.in/@DmPanf)

---

⭐ *If you like this project, don’t forget to star the repo!*

