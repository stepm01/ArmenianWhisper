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

---

## 🗺️ Project Structure (planned)

```
.
├── data/                # Raw and processed datasets (ignored)
├── models/              # Fine-tuned checkpoints and adapters
├── notebooks/           # Exploration, evaluation, and alignment notebooks
├── scripts/             # Dataset download, cleaning, and training helpers
├── server/              # FastAPI backend
└── web/                 # Frontend prototype (Svelte or React)
```

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
git clone https://github.com/YOUR_USERNAME/armenian-whisper.git
cd armenian-whisper
git checkout tester
bash scripts/download_data.sh
```

> ℹ️ Replace `YOUR_USERNAME` with the correct GitHub handle. The `scripts/download_data.sh` helper will pull the core datasets once implemented; for now, follow the dataset notes in `scripts/`.

---

## 📊 Evaluation Toolkit (planned)

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

## 🤝 Contributing

Ideas, datasets, evaluation feedback, and GPU time are all welcome. Open an issue or start a discussion if you would like to collaborate or share benchmarks.

---

## 📬 Stay in the Loop

Watch the repository or subscribe to project updates to follow along. Progress notes, training lessons, and demo clips will be shared once the first end-to-end pipeline is live.
