import { writable } from 'svelte/store';

export type TranscriptionSegment = {
  start: number;
  end: number;
  text_hy: string;
  text_en?: string;
};

export type TranscriptionJob = {
  job_id: string;
  status: string;
  language: string;
  segments: TranscriptionSegment[];
  translated: boolean;
};

export const job = writable<TranscriptionJob | null>(null);
