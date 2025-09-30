# ArmenianWhisper

🎙️ **AI-powered Armenian Speech-to-English Subtitle Generator**

ArmenianWhisper is an open summer project that turns Armenian speech into accurate English subtitles. By pairing OpenAI Whisper with lightweight fine-tuning and community-curated datasets, it aims to make Armenian cultural content easier to share, archive, and access.

---

## 📌 Overview

- Focuses on low-resource Armenian speech recognition and translation.
- Builds an end-to-end subtitle pipeline: transcription → alignment → translation.
- Prioritizes reproducibility so others can extend or adapt the work.
- Designed as a summer sprint with week-by-week milestones.

---

## 🧠 Motivation

Armenian remains underrepresented across modern AI tooling. ArmenianWhisper explores how open-source models and targeted LoRA fine-tuning can improve accessibility for Armenian audio content. The project blends language preservation, open research, and practical tooling for creators and archivists.

---

## 🌟 Feature Goals

- High-quality Armenian ASR with strong accent coverage.
- Reliable English subtitle generation with timing alignment (WhisperX).
- Evaluation dashboards for BLEU, WER, and latency metrics.
- Lightweight FastAPI backend for serving transcription + translation.
- Simple web UI prototype for uploading audio and exporting subtitles.

---

## 🔧 Tech Stack

- 🤖 **Model**: OpenAI Whisper `small` with LoRA fine-tuning
- ⚡ **Inference**: Faster-Whisper / CTranslate2
- 🧹 **Datasets**: Common Voice v17 (hy), OpenSLR 154, FLEURS-hy, plus scraped YouTube clips
- 🧱 **Backend**: FastAPI
- 🎛️ **Frontend**: Svelte or React (planned)
- ☁️ **Deployment**: Fly.io or Docker (planned)

## 🗣️ Languages in Play

| Language | Role |
|----------|------|
| Armenian (hy-AM) | Primary transcription input (Eastern + Western dialects) |
| English (en) | Subtitle + translation output |
| Python | Data prep, training scripts, FastAPI backend |
| Bash | Dataset automation scripts |
| HTML / TypeScript / Svelte | Web UI and interaction layer |

## 🧠 Models & Tooling

| Component | Library or Tooling |
|-----------|-------------------|
| Base ASR model | openai/whisper-small |
| Fine-tuning | LoRA via `peft` + `transformers` |
| Inference optimisation | Faster-Whisper (CT2 backend) |
| Alignment | WhisperX for word-level timestamps |
| Translation fallback | Meta NLLB-200 (optional) |
| Data pipeline | `datasets`, `torchaudio`, custom scripts |
| Deployment targets | Docker, Fly.io, GPU notebooks |
| Frontend framework | Svelte + Vite |

---

## 📁 Current Repository Layout

````text
.
├── README.md
├── .gitignore
├── app/                # FastAPI backend scaffold
│   ├── api/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── tests/
├── data/               # Raw datasets tracked via .gitkeep
│   └── raw/
├── docs/               # Reporting artifacts (e.g., dataset stats)
├── notebooks/          # Exploratory analysis notebooks
├── scripts/            # Automation helpers (download, preprocessing)
└── web/                # Svelte + Vite frontend prototype
    └── src/lib/components
````

---

## 📊 Datasets in Scope

| Dataset | Source | Est. Hours | Notes |
|---------|--------|-----------|-------|
| Common Voice v17 (hy) | Mozilla / Hugging Face | ~45 h | Community accents, read speech |
| OpenSLR #154 | OpenSLR | ~35 h | Audiobook recordings |
| FLEURS (hy-AM) | Google / Hugging Face | ~2 h | Evaluation split |
| YouTube scraped (planned) | Public corpus | +50 h (target) | Conversational + interview audio |

## 📦 Target Outputs

- Upload audio or paste a YouTube URL → receive `.srt` / `.vtt` subtitles.
- Dual-language transcripts (Armenian + English) for archive workflows.
- Interactive subtitle timeline with word-level alignment.
- Reproducible notebooks covering training, evaluation, and error analysis.

## 🧪 Evaluation Targets

| Metric | Target | Notes |
|--------|--------|-------|
| Word Error Rate (WER) | ≤ 18% | Held-out Common Voice dev split |
| BLEU (translation) | ≥ 40 | Evaluated on FLEURS hy→en |
| Timestamp drift | ≤ 0.5 sec | Average misalignment (WhisperX) |
| Inference latency | < 5× realtime (CPU) | Aim for 1× on GPU |

---

## 🗓️ 10-Week Roadmap

| Week | Focus |
|------|-------|
| 1 | Set up dev environment; download and inspect datasets |
| 2 | Build a YouTube scraper for Armenian speech clips |
| 3 | Clean and quality-check aggregated datasets |
| 4 | Run LoRA fine-tuning on Whisper-small |
| 5 | Perform alignment (WhisperX) and evaluate BLEU/WER |
| 6 | Improve translation quality and add fallback pipelines |
| 7 | Implement the FastAPI backend |
| 8 | Prototype the frontend |
| 9 | Deploy with 8-bit quantization |
| 10 | Ship blog post, demo, and wrap-up 📽️ |

---

## 🚀 Quick Start

```bash
# 1. Clone + switch to the collaboration branch
git clone https://github.com/YOUR_USERNAME/armenian-whisper.git
cd armenian-whisper
git checkout tester

# 2. (Optional) stage dataset downloads
bash scripts/download_data.sh

# 3. Spin up the FastAPI backend
python -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8000

# 4. In a second terminal, run the Svelte dev server
cd web
npm install
npm run dev -- --open
```

> ℹ️ Replace `YOUR_USERNAME` with the correct GitHub handle. The dataset script is a placeholder until authenticated downloads are automated.

---

## 🧰 Evaluation Toolkit (roadmap)

- BLEU and WER tracking notebooks in `notebooks/`.
- Alignment inspection via WhisperX outputs.
- Latency profiling for CPU/GPU inference paths.

---

## 🛠️ Next Milestones

- [ ] Publish dataset download and cleaning scripts.
- [ ] Draft evaluation notebooks for BLEU/WER tracking.
- [ ] Stand up a FastAPI prototype with a translation endpoint.
- [ ] Explore lightweight UI concepts (Svelte vs React).

---

## 📜 License & Usage

- Code is released under the MIT License.
- Datasets remain under their original Creative Commons or public licenses.
- YouTube scraping stores metadata only—do not redistribute raw audio.

---

## 🤝 Contributing

Ideas, datasets, evaluation feedback, and GPU time are all welcome. Open an issue or start a discussion if you would like to collaborate or share benchmarks.

---

## 📬 Stay in the Loop

Watch the repository or subscribe to project updates to follow along. Progress notes, training lessons, and demo clips will be shared once the first end-to-end pipeline is live.
