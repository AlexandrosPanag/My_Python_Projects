# 🎬 WebM Megasolution

A simple all-in-one command-line toolkit for processing `.webm` video files. Sharpen, compress, boost frame rate, or run the full pipeline in a single command — no GUI needed.

> Written by [Alexandros Panagiotakopoulos](https://alexandrospanag.github.io)
> LICENSE: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Features

| Option | Function | Description |
|--------|----------|-------------|
| `1` | **Sharpen** | Applies a subtle unsharp mask to reduce pixelation and crisp up edges |
| `2` | **Compress** | Minimises file size using VP9 CRF encoding + Opus audio |
| `3` | **Fluidity** | Boosts frame rate via motion-compensated frame interpolation |
| `4` | **All-in-one** | Runs Sharpen → Fluidity → Compress in sequence |

---

## Requirements

### Python
Python 3.7 or higher. No third-party Python packages are required — only the standard library.

### FFmpeg
This script is a wrapper around [FFmpeg](https://ffmpeg.org/). You must have the FFmpeg binary installed and accessible.

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Using winget
winget install FFmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt install ffmpeg
```

After installing, verify it works:
```bash
ffmpeg -version
```

---

## Installation

No installation required. Just download the script and run it.

```bash
git clone https://github.com/your-username/webm-megasolution.git
cd webm-megasolution
```

Or download `WebM_megasolution.py` directly and place it in your working directory.

---

## Usage

```bash
python WebM_megasolution.py input.webm [output.webm]
```

The output file argument is optional. If omitted, the script generates a name automatically based on the operation performed (e.g. `video_sharpened.webm`, `video_compressed.webm`).

### Example

```
$ python WebM_megasolution.py myclip.webm

╔══════════════════════════════════════╗
║         WebM Toolkit  v1.0           ║
╠══════════════════════════════════════╣
║  1 → Sharpen   (reduce pixelation)   ║
║  2 → Compress  (minimise file size)  ║
║  3 → Fluidity  (boost frame rate)    ║
║  4 → All-in-one (1 → 3 → 2)         ║
╚══════════════════════════════════════╝

Enter your choice (1/2/3/4):
```

---

## Options in Detail

### 1 — Sharpen
Applies FFmpeg's `unsharp` filter with gentle settings designed to reduce blocky compression artifacts without introducing halos or noise. Chroma sharpening is disabled to avoid colour fringing.

- Filter: `unsharp=5:5:0.4:5:5:0.0`
- Codec: VP9 (`libvpx-vp9`), CRF 23
- Audio: copied as-is (no re-encode)
- Output: `<name>_sharpened.webm`

### 2 — Compress
Aggressively reduces file size while preserving the original resolution. Uses VP9's constant quality mode with a high CRF value and re-encodes audio to Opus at 64 kbps.

- Codec: VP9 (`libvpx-vp9`), CRF 35
- Audio: Opus (`libopus`) at 64 kbps stereo
- Multithreading enabled (`row-mt`, `tile-columns`)
- Output: `<name>_compressed.webm`

> **Tip:** You can adjust the CRF value in the source code. The range is 18–40 — higher values produce smaller files at the cost of quality.

### 3 — Fluidity (Frame Rate Boost)
Synthesises new in-between frames using motion-compensated frame interpolation (MCFI), making motion appear noticeably smoother. You will be prompted to enter a target FPS (default: 60).

- Filter: `minterpolate` with `mi_mode=mci`, `mc_mode=aobmc`, bidirectional motion estimation
- Codec: VP9 (`libvpx-vp9`), CRF 23
- Audio: copied as-is
- Output: `<name>_fluid_60fps.webm`

> ⚠️ **Note:** Frame interpolation is computationally expensive. Processing time scales with video length and resolution. A 1-minute 1080p clip may take several minutes.

### 4 — All-in-one
Chains all three operations in the optimal order: **Sharpen → Fluidity → Compress**. The compression step is intentionally last to avoid re-compressing already-compressed frames from earlier steps. Intermediate files are created temporarily and deleted automatically on completion.

- Output: `<name>_processed.webm`

---

## Output File Naming

If no output path is specified, files are named automatically:

| Option | Output name |
|--------|-------------|
| 1 | `<input>_sharpened.webm` |
| 2 | `<input>_compressed.webm` |
| 3 | `<input>_fluid_60fps.webm` |
| 4 | `<input>_processed.webm` |

---

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to share and adapt the material for non-commercial purposes, as long as you give appropriate credit and distribute any derivatives under the same license.
