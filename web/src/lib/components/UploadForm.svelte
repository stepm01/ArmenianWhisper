<script lang="ts">
  import axios from 'axios';
  import type { TranscriptionJob } from '../stores/transcription';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher<{ jobCreated: TranscriptionJob }>();

  let file: File | null = null;
  let isSubmitting = false;
  let error: string | null = null;

  const onFileChange = (event: Event) => {
    const input = event.target as HTMLInputElement;
    file = input.files?.[0] ?? null;
    error = null;
  };

  const submit = async () => {
    if (!file) {
      error = 'Please select an audio file before submitting.';
      return;
    }
    const formData = new FormData();
    formData.append('file', file);

    try {
      isSubmitting = true;
      const response = await axios.post('/api/transcribe', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      dispatch('jobCreated', response.data as TranscriptionJob);
      error = null;
    } catch (err) {
      error = 'Failed to submit job. Ensure the backend is running.';
      console.error(err);
    } finally {
      isSubmitting = false;
    }
  };
</script>

<div class="card">
  <h2>Upload audio</h2>
  <p>Accepted formats: WAV, MP3, FLAC, M4A. Max upload size 200 MB.</p>

  <input aria-label="Upload audio" type="file" accept="audio/*" on:change={onFileChange} />

  <button class="submit" on:click|preventDefault={submit} disabled={isSubmitting}>
    {#if isSubmitting}
      Submitting…
    {:else}
      Transcribe
    {/if}
  </button>

  {#if error}
    <p class="error">{error}</p>
  {/if}
</div>

<style>
  .card {
    background: white;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    padding: 1.5rem;
    box-shadow: 0 20px 25px -20px rgba(15, 23, 42, 0.2);
  }

  h2 {
    margin-bottom: 0.25rem;
  }

  input[type='file'] {
    margin: 1rem 0;
  }

  .submit {
    background: linear-gradient(135deg, #d946ef, #6366f1);
    color: white;
    padding: 0.75rem 1.5rem;
  }

  .submit:disabled {
    background: #cbd5f5;
    cursor: not-allowed;
  }

  .error {
    color: #dc2626;
    margin-top: 0.75rem;
  }
</style>
