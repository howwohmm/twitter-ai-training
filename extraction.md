# Twitter AI Training

## project name + description
- twitter-ai-training: Train a custom GPT on 1000+ like viral tweets to generate high-engagement Twitter posts autonomously overnight

## who it's for
- Building Twitter presence without manual writing; personal use for generating and posting tweets

## current status
- in progress — experimental / active research; data collection phase

## what was actually built
- Data collection pipeline: Twitter Advanced Search (min_faves:1000) → manual copy-paste → raw-tweets.txt (61 lines) → twitter_simple.txt (143 lines cleaned)
- twitter_finetune.json — structured training data format
- bookmarks-training.txt — additional training data from bookmarks
- autoresearch-macos framework integration: Claude Code acts as autonomous research agent, modifies train.py, runs 30–50 experiments per night on Apple Silicon MPS
- PyTorch GPT trained on MPS (Apple Silicon) using nanochat as base
- Evaluation metric: val_bpb (bits per byte, vocab-size-independent — lower is better)
- Generation workflow: load best checkpoint → run generate.py → get 10 options → pick best 3 → edit 20-30% → post
- CLAUDE.md with slash commands: /collect, /train, /generate, /status
- models/ and generated/ directories for checkpoints and outputs (currently empty — training not yet run to completion)

## why it was built
- To automate generating high-signal Twitter content without manual writing; using autonomous overnight training to iterate quickly on model quality

## blockers or reasons shelved
- Data collection is manual and slow — only ~50-100 tweets collected, need 500+ for quality training
- Generated output still requires 20-30% human editing before posting
- models/ and generated/ are empty — no successful training run completed yet

## wins or progress moments
- autoresearch-macos framework set up for autonomous overnight Claude Code runs (30–50 experiments per night while sleeping)
- Evaluation metric (val_bpb) chosen to be vocab-size-independent — good ML practice
- Quality threshold defined: only 1000+ like tweets in training data

## pain points
- No Twitter API — data collection is entirely manual copy-paste
- Need 500+ tweets but have ~50-100 — 5-10x more data collection needed before training is meaningful
- 30% editing threshold means generated output isn't drop-in ready

## where claude api / ai was used or planned
- Claude Code as the autonomous overnight research agent — runs autoresearch-macos, modifies train.py, iterates on hyperparameters across 30-50 experiments per night
- The trained GPT model itself generates tweet candidates (not Claude)

## what would've helped
- Twitter API access for automated data collection (scraping 1000+ like tweets at scale)
- A way to evaluate tweet quality beyond val_bpb — e.g. human preference scoring
- More training data: 500+ tweets minimum before the model has enough signal

## metrics or traction
- none yet — no training runs completed, no tweets generated or posted
