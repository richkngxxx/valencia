"""Pre-generates audio/<hash>.mp3 with Matxa-TTS multiaccent (projecte-aina, BSC), Valencian voice.
Needs: espeak-ng >=1.52 (ca-va), onnxruntime, phonemizer, the e2e ONNX model and the cleaners from
github.com/langtech-bsc/minimal-tts-api (text/). Usage: python3 gen_audio.py TTS_DIR [workers] [speaker]"""
import sys, os, json, subprocess, tempfile
from concurrent.futures import ProcessPoolExecutor
TTS = sys.argv[1]; sys.path.insert(0, TTS)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."); OUT = os.path.join(ROOT, "audio")
SPK = int(sys.argv[3]) if len(sys.argv) > 3 else 7  # 6 = lluc, 7 = gina (valencià)
S = None
def init():
    global S
    import onnxruntime as ort
    o = ort.SessionOptions(); o.intra_op_num_threads = 2; o.inter_op_num_threads = 1
    S = ort.InferenceSession(os.path.join(TTS, "e2e.onnx"), o, providers=["CPUExecutionProvider"])
def job(it):
    import numpy as np, soundfile as sf
    from text import text_to_sequence
    f = os.path.join(OUT, it["h"] + ".mp3")
    if os.path.exists(f): return it["h"], None
    t = it["text"].strip()
    if t[-1] not in ".?!": t += "."
    t = ", " + t  # a leading pause stops the model from swallowing the first consonant
    seq = text_to_sequence(t, ["catalan_valencia_cleaners"]); x = [0] * (2 * len(seq) + 1); x[1::2] = seq
    x = np.array(x, dtype=np.int64)[None]
    _, w = S.run(None, {"x": x, "x_lengths": np.array([x.shape[1]], dtype=np.int64),
                        "scales": np.array([0.2, 1.1], dtype=np.float32), "spks": np.array([SPK])})
    w = w.squeeze()
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        sf.write(tmp.name, w, 22050)
        trim = "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,adelay=60,apad=pad_dur=0.12"
        ok = False
        for norm in (",loudnorm=I=-18:TP=-1.5", ",alimiter=limit=0.85", ""):  # lame occasionally asserts on loudnorm output
            r = subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp.name, "-af", trim + norm,
                "-ac", "1", "-ar", "22050", "-c:a", "libmp3lame", "-b:a", "32k", f + ".tmp.mp3"], capture_output=True)
            if r.returncode == 0: ok = True; break
    if not ok:
        if os.path.exists(f + ".tmp.mp3"): os.remove(f + ".tmp.mp3")
        return it["h"], -1
    os.replace(f + ".tmp.mp3", f)
    return it["h"], len(w) / 22050
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    items = json.loads(subprocess.check_output(["node", os.path.join(ROOT, "tools/audio_texts.js")]))
    with ProcessPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 3, initializer=init) as ex:
        for i, (h, d) in enumerate(ex.map(job, items, chunksize=8)):
            if i % 100 == 0 or d == -1: print(i, h, d, flush=True)
    keep = {it["h"] for it in items}
    for fn in os.listdir(OUT):
        if fn.endswith(".mp3") and fn[:-4] not in keep: os.remove(os.path.join(OUT, fn))
    man = {"voice": "Matxa-TTS multiaccent · valencià (gina)", "licence": "projecte-aina/BSC — ús no comercial", "items": {it["key"]: it["h"] for it in items if os.path.exists(os.path.join(OUT, it["h"] + ".mp3"))}}
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("done", len(items))
