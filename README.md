# Dual-Vector VR Polygraph AI Engine

This repository contains the foundational core algorithm for a **Dual-Vector Virtual Reality Polygraph System** designed for remote therapeutic monitoring and clinical biofeedback. 

The engine processes simultaneous inputs from **Acoustic Voice Stress Analysis (VSA)** and **Optical PPG Sensors** inside a VR headset to calculate a real-time **Cognitive Friction & Sincerity Index (CFSI)**.

## 🚀 System Architecture
- **Hardware Layer:** Integrated VR headset mouthpiece port + internal cushion PPG infrared sensor.
- **Processing Layer:** Dual-vector data synchronization utilizing a time-aligned data window to catch immediate vocal tremors and lagging autonomic cardiac changes.
- **Frontend Dashboard:** A clean, clinical web tool optimized for remote therapists using WebRTC streaming protocols.

## 📁 Repository Structure
- `engine.py` - Core AI calculation scoring module with safety fail-safes.
- `README.md` - Documentation, system architecture specification, and setup guide.

## 💻 Core Code Example (`engine.py`)
```python
def calculate_sincerity_index(audio_baseline_tremor, audio_response_tremor, hrv_baseline, hrv_response):
    """
    Calculates the Cognitive Friction & Sincerity Index (CFSI).
    Weights: 45% Acoustic Delta, 45% Cardiac Stability (HRV), 10% Baseline.
    """
    # Calculate Voice Stress (Drop in micro-tremors 8Hz-12Hz)
    tremor_loss = audio_baseline_tremor - audio_response_tremor
    acoustic_score = max(0.0, 1.0 - (tremor_loss * 2.5)) 
    
    # Calculate Heart Stress (Drop in Heart Rate Variability)
    hrv_drop = hrv_baseline - hrv_response
    cardiac_score = max(0.0, 1.0 - (hrv_drop / hrv_baseline))
    
    # Core Fusion Formula 
    final_index = (acoustic_score * 0.45) + (cardiac_score * 0.45) + 0.10
    
    return round(final_index * 100, 1)
```

## 🛡️ Anti-False-Positive Fail-safes
1. **The Caffeine Override:** Automatically shifts weighting calculations if a patient's baseline heart rate is exceptionally high (e.g., from highly concentrated local native coffee) to prevent false-positive stress tracking.
2. **The Panic Dampener:** Disregards initial startle reflexes that stabilize within a 2-second window.

---
*Developed by the Lead Systems Architecture & Engineering Team.*
