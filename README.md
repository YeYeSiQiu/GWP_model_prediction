# GWP_model_prediction

This repository contains the code, data, and documentation for the prediction model of concrete Global Warming Potential (GWP), developed as part of a research project exploring the environmental impact of CaCS (Carbonate-containing Cement Substitution) in concrete production.

---

## 📌 Project Background

Concrete production is a major contributor to global CO₂ emissions, largely due to the high carbon footprint of cement. This model estimates GWP per cubic meter of concrete by incorporating:

1. **Cement reduction** via CaCO₃ substitution  
2. **CO₂ sequestration** through CaCS carbonation  
3. **Other lifecycle emissions** including aggregate, admixtures, and transport

This repository supports the results and methods described in Section **2.3.4** and Figure **3.2** of our publication.

---

## ⚙️ Model Equation

The total GWP is computed as:

```
GWP_total = m_c · EF_c + m_CaCO₃ · EF_CaCO₃ + m_a · EF_a + EF_admix + EF_trans − CO₂_sequestration
```

Where:

- `m_c`: Cement content (kg/m³)  
- `EF_c`: Emission factor for cement (e.g., 0.9 kg CO₂-eq/kg)  
- `m_CaCO₃`: Substituted CaCO₃ mass (kg/m³)  
- `m_a`: Aggregate content (kg/m³)  
- `EF_*`: Emission factors of individual stages  
- `CO₂_sequestration`: CO₂ fixed by CaCS reaction

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `GWP_model_prediction.py` | Python script to calculate and visualize GWP |
| `Supplementary_Table_S2_GWP_Data.xlsx` | Simulated GWP values across strength/substitution ranges |
| `README.md` | Project description and usage guide |
| `requirements.txt` | Python dependencies |

---

## 📊 Visualization

The code produces a 3D surface plot to illustrate the relationship between:
- **Concrete strength** (C30–C60)
- **CaCO₃ substitution rate** (5%–30%)
- **Resulting GWP values**

The output can be regenerated using the script `GWP_model_prediction.py`.

---

## ▶️ Usage Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YeYeSiQiu/GWP_model_prediction.git
cd GWP_model_prediction
```

### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Run the model
```bash
python GWP_model_prediction.py
```

---

## 🔍 Citation

If you use this model or data in your work, please cite the corresponding publication:

> [Haimeifabiao,not public yet], *Title*, Journal Name, Year, DOI

---

## 📬 Contact

For questions or collaborations, please contact:  
**[Jiahui]**  
Email: [Jiahui.Zhu@Ugent.be]  
Affiliation: [Ugent]
