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
  <header>
    <h1>ArmenianWhisper Translator</h1>
    <p>
      Upload Armenian audio, generate English subtitles, and preview aligned segments. The backend
      is a FastAPI service that wraps a Whisper + LoRA pipeline.
    </p>
  </header>

  <section>
    <UploadForm on:jobCreated={(event) => handleJobCreated(event.detail)} />
  </section>

  <section>
    <TranscriptPreview />
  </section>
</main>

<style>
  h1 {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 0.5rem;
  }

  p {
    max-width: 720px;
    color: #475569;
  }

  section + section {
    margin-top: 2.5rem;
  }
</style>
