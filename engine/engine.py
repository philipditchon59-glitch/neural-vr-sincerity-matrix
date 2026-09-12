pythonimport time

def initialize_system_handshake():
    """
    Simulates the physical hardware boot loop and connection matrix.
    Prints the custom 2035 cyberpunk device handshake protocols.
    """
    print("==================================================================")
    print("[SYSTEM HANDSHAKE SECURE] ➔ [LATENCY: 1.2ms] ➔ [MODE: BIO-THERAPY]")
    print("[Mouthpiece Micro-Port: ACTIVE]")
    print("[Quantum PPG Cushion: SCANNING INFRARED CAPILLARIES]")
    print("==================================================================\n")

def calculate_cyberpunk_sincerity_matrix(
    audio_baseline, audio_response, 
    hrv_baseline, hrv_response, 
    time_to_stabilize_seconds, is_caffeine_detected=False
):
    """
    Advanced Biometric Core with Fail-Safe Intercept.
    Protects against false positives from coffee spikes and startle reflexes.
    """
    # --- FAIL-SAFE 1: THE PANIC DAMPENER (STARTLE REFLEX INTERCEPT) ---
    # If the patient's system spikes but recovers within a 2-second window,
    # the algorithm bypasses the panic penalty.
    if time_to_stabilize_seconds <= 2.0:
        print("[🛡️ FAIL-SAFE ACTIVATED]: Initial Startle Reflex Detected & Dampened.")
        return 100.0

    # Calculate raw structural drops
    tremor_loss = audio_baseline - audio_response
    acoustic_score = max(0.0, 1.0 - (tremor_loss * 2.5))
    
    hrv_drop = hrv_baseline - hrv_response
    cardiac_score = max(0.0, 1.0 - (hrv_drop / hrv_baseline))

    # --- FAIL-SAFE 2: THE CAFFEINE OVERRIDE ---
    # If the user has high native coffee levels, the heart rhythm is already rigid.
    # We dynamically shift the weights to rely heavier on voice (70%) than heart (20%).
    if is_caffeine_detected:
        print("[☕ CAFFEINE FAIL-SAFE]: Heart telemetry compressed. Recalibrating weights...")
        voice_weight = 0.70
        heart_weight = 0.20
    else:
        voice_weight = 0.45
        heart_weight = 0.45

    # Core Fusion Calculation Matrix
    final_index = (acoustic_score * voice_weight) + (cardiac_score * heart_weight) + 0.10
    return round(final_index * 100, 1)


# ==================================================================
# 🧪 PRODUCTION TEST PIPELINE - NEON VERITAS CORE ENGINE
# ==================================================================

# 1. Trigger the Hardware Connection Status 
initialize_system_handshake()

# 2. Process Telemetry Test Scenarios
print("--- RUNNING SIMULATION 1: Sudden Startle (Recovers in 1.5s) ---")
run_1 = calculate_cyberpunk_sincerity_matrix(
    audio_baseline=8.0, audio_response=5.0, 
    hrv_baseline=78.0, hrv_response=29.0,
    time_to_stabilize_seconds=1.5
)
print(f"Matrix Sincerity Score: {run_1}%\n")

print("--- RUNNING SIMULATION 2: Sustained Stress + Native Coffee Active ---")
run_2 = calculate_cyberpunk_sincerity_matrix(
    audio_baseline=8.0, audio_response=5.0, 
    hrv_baseline=78.0, hrv_response=29.0,
    time_to_stabilize_seconds=5.0,
    is_caffeine_detected=True 
)
print(f"Matrix Sincerity Score: {run_2}%")
print("==================================================================")
