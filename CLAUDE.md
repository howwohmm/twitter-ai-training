# Twitter AI Training Project

## Mission
Build an AI that generates high-signal Twitter posts trained on viral tweets.

## Tech Stack
- **Framework:** autoresearch-macos (autonomous ML training)
- **Model:** GPT-based language model
- **Training:** PyTorch with MPS (Apple Silicon)
- **Data:** Curated viral tweets (1000+ likes each)

## Project Structure
```
twitter-ai-project/
├── autoresearch-macos/     # Training framework
├── data/
│   ├── raw-tweets.txt      # Collected tweets
│   └── training-ready.txt  # Cleaned for training
├── models/                 # Trained model checkpoints
└── generated/              # Generated tweet outputs
```

## Workflows

### Data Collection (Manual)
1. Use Twitter Advanced Search with `min_faves:1000`
2. Copy-paste 50-100 viral tweets
3. Save to `data/raw-tweets.txt`
4. Separate with `---`

### Training (Autonomous)
1. Copy data to autoresearch: `cp data/training-ready.txt autoresearch-macos/data/train.txt`
2. Prepare: `uv run prepare.py`
3. Start Claude Code autonomous training overnight
4. Review experiments in morning

### Generation
1. Load best checkpoint
2. Run generate.py with prompts
3. Get 10 options, pick best 3
4. Edit 20-30%, post

## Commands
- `/collect` - Instructions for collecting viral tweets
- `/train` - Start autonomous overnight training
- `/generate` - Generate tweets from trained model
- `/status` - Check training progress

## Quality Standards
- Training data: ONLY tweets with 1000+ likes
- Generated output: Must pass "scroll-stopping" test
- Editing threshold: 30% max (if more, retrain)

## Success Metrics
- val_bpb: Lower = better (track in experiments)
- Generated quality: Hooks grab attention in 5 words
- Engagement: Track real performance of posted tweets

## Notes
- Start with 50 tweets, iterate to 500+
- Quality > Quantity for training data
- Claude Pro enables autonomous overnight optimization
- Expect 30-50 experiments per night
