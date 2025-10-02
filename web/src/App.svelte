<script lang="ts">
  import UploadForm from './lib/components/UploadForm.svelte';
  import TranscriptPreview from './lib/components/TranscriptPreview.svelte';
  import type { TranscriptionJob } from './lib/stores/transcription';
  import { job } from './lib/stores/transcription';

  const handleJobCreated = (payload: TranscriptionJob) => {
    job.set(payload);
  };
</script>

<main>
  <header class="hero">
    <img class="logo" src="/logo.png" alt="ArmenianWhisper logo" />
    <div>
      <h1>ArmenianWhisper Translator</h1>
      <p class="subtitle">Created by Stepan Muradkhanyan</p>
      <p>
        Upload Armenian audio, generate English subtitles, and preview aligned segments. The backend
        is a FastAPI service that wraps a Whisper + LoRA pipeline.
      </p>
    </div>
  </header>

  <section>
    <UploadForm on:jobCreated={(event) => handleJobCreated(event.detail)} />
  </section>

  <section>
    <TranscriptPreview />
  </section>
</main>

<style>
  .hero {
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }

  .logo {
    width: clamp(96px, 14vw, 148px);
    height: auto;
    border-radius: 16px;
    box-shadow: 0 12px 25px -12px rgba(15, 23, 42, 0.35);
  }

  h1 {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 0.5rem;
  }

  p {
    max-width: 720px;
    color: #475569;
  }

  .subtitle {
    margin: 0.25rem 0 0.75rem;
    font-weight: 500;
    color: #1e3a8a;
  }

  section + section {
    margin-top: 2.5rem;
  }

  @media (max-width: 640px) {
    .hero {
      flex-direction: column;
      text-align: center;
    }

    .logo {
      width: 120px;
    }
  }
</style>
