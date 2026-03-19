# twitter-ai-training

Pipeline to collect viral tweets, format them as training data, and fine-tune a GPT on them using PyTorch on Apple Silicon MPS.

## What it is

The goal: train a small language model on tweets with 1000+ likes, so it learns the structure and voice of high-signal content. Then use it to generate tweet drafts.

Not trying to replace judgment — the output is raw material to edit.

## How it works

**Data collection (manual):**
- Twitter Advanced Search: `min_faves:1000`
- Copy 50–100 tweets into `data/raw-tweets.txt`, separated by `---`

**Training:**
- Uses `autoresearch-macos` as the training framework (autonomous ML, runs overnight)
- Data prepped via `prepare.py` → `data/train.txt`
- PyTorch with MPS backend for Apple Silicon GPU acceleration
- Runs 30–50 experiments per session, tracks `val_bpb` (lower = better)

**Generation:**
- Load best checkpoint
- `generate.py` with a prompt → 10 options
- Pick 3, edit 20–30%, post

## Training data format

`data/twitter_finetune.json` — structured JSONL with tweet text and metadata for fine-tuning.

## Tech

- PyTorch (MPS — Apple Silicon)
- Custom GPT architecture (small, fast to train locally)
- `autoresearch-macos` training framework

## Status

In progress. First training runs done. Working on scaling the dataset from ~50 to 500+ tweets.

## Quality bar

Only tweets with 1000+ likes go in. If generated output needs >30% editing, retrain with more data.
