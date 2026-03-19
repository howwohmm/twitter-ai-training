# Twitter AI Training

**status:** experimental / active research

**what:** Train a GPT on 1000+ like viral tweets, generate novel high-engagement posts. Uses autoresearch-macos for autonomous overnight training with Claude Code as the research agent.

**for:** building Twitter presence without manual writing

**built:**
- data collection: Twitter Advanced Search (min_faves:1000) → training-ready.txt
- autoresearch-macos framework: Claude modifies train.py, runs 30–50 experiments/night
- PyTorch GPT on Apple Silicon MPS
- eval metric: val_bpb (lower = better, vocab-size-independent)
- workflow: collect → train → generate → edit 20-30% → post

**tech:** PyTorch, MPS (Apple Silicon), Python, uv, nanochat base

**ai:** Claude Code as autonomous overnight research agent

**blockers:**
- data collection is manual (need 500+ tweets, have ~50-100)
- generated output still needs 20-30% editing

**tools/autoresearch-macos:** the framework lives at ../tools/autoresearch-macos/
