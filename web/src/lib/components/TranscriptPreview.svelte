<script lang="ts">
  import { derived } from 'svelte/store';
  import { job } from '../stores/transcription';

  const summary = derived(job, ($job) => {
    if (!$job) return null;
    const totalSeconds = $job.segments.reduce((acc, segment) => acc + (segment.end - segment.start), 0);
    return {
      segments: $job.segments.length,
      totalSeconds,
      translated: $job.translated,
    };
  });
</script>

<div class="panel">
  <h2>Transcript preview</h2>
  {#if $summary && $summary.segments > 0}
    <p>
      {$summary.segments} segments • {(Math.round($summary.totalSeconds * 10) / 10).toFixed(1)} seconds •
      {#if $summary.translated}Translated to English{/if}
    </p>

    <ol>
      {#each $job?.segments ?? [] as segment, index}
        <li>
          <header>
            <span>{index + 1}</span>
            <time>{segment.start.toFixed(1)}s → {segment.end.toFixed(1)}s</time>
          </header>
          <p class="hy">{segment.text_hy}</p>
          {#if segment.text_en}
            <p class="en">{segment.text_en}</p>
          {/if}
        </li>
      {/each}
    </ol>
  {:else}
    <p>No transcription yet. Submit an audio file to preview subtitles.</p>
  {/if}
</div>

<style>
  .panel {
    background: white;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    padding: 1.5rem;
  }

  ol {
    margin: 1.5rem 0 0;
    padding: 0;
    list-style: none;
    display: grid;
    gap: 1.5rem;
  }

  li {
    border-left: 4px solid #a855f7;
    padding-left: 1rem;
  }

  header {
    display: flex;
    justify-content: space-between;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #475569;
  }

  .hy {
    font-weight: 600;
  }

  .en {
    color: #334155;
    margin-top: 0.25rem;
  }
</style>
