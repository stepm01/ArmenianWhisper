#!/usr/bin/env bash
set -euo pipefail

# Placeholder script for downloading Armenian speech datasets.
# Requires: wget, git, and huggingface-cli (for authenticated datasets).

DATA_ROOT="${DATA_ROOT:-$(pwd)/data/raw}"
mkdir -p "$DATA_ROOT"

print_step() {
  printf '\n[%s] %s\n' "$(date +"%H:%M:%S")" "$1"
}

print_step "Preparing dataset directories at $DATA_ROOT"

# TODO: Automate downloads for Common Voice, OpenSLR, and FLEURS.
print_step "Downloading Common Voice v17 (hy)..."
echo "- Use huggingface-cli to authenticate and download the dataset."

echo "huggingface-cli datasets download --repo datasets/mozilla-foundation/common_voice_17_0 --name hy --local-dir $DATA_ROOT/commonvoice_v17" && printf '\n'

print_step "Downloading OpenSLR #154 (Audiobooks)..."
echo "- Fetch tarball from http://www.openslr.org/154/ and extract to $DATA_ROOT/openslr_154" && printf '\n'

print_step "Downloading Google FLEURS (hy-AM)..."
echo "- Use huggingface-cli to pull google/fleurs and filter for hy_am" && printf '\n'

print_step "All dataset downloads completed (placeholder)."
print_step "Remember to verify licenses and respect usage policies."
