# Golf Swing Position Classification

## Project structure

```
notebooks/
├── 01_data_pipeline.ipynb           # GolfDB filtering, MediaPipe pose extraction, splits
├── 02_classifiers.ipynb             # Three classifiers: Pose+ML, CNN, GPT-5 mini
├── 03_cross_model_comparison.ipynb  # Side-by-side analysis
└── 04_coaching_agent.ipynb          # Pro reference, deviation analysis, RAG, agent

data/
├── raw/                             # GolfDB source files (videos + metadata)
├── processed/                       # Phase 1 outputs (frames, keypoints, splits)
├── results/                         # Phase 2/3 prediction outputs and metrics
├── coaching_corpus/                 # 16 markdown coaching documents
└── chroma_db/                       # Phase 4 vector store

scripts/                             # One-off setup golfdb and verification scripts
```

## Reproducing the project

1. Set up `.env` at root:
   ```
   OPENAI_API_KEY=sk-...
   ```

3. Download the GolfDB `videos_160` dataset to `data/raw/videos_160/` and the metadata files to `data/raw/golfDB.pkl` and `data/raw/golfDB.mat`.

4. Run notebooks in order from `notebooks/`. Each notebook is self-contained but assumes the previous one's outputs exist in `data/processed/` and `data/results/`.


Manual overwride of protobuf version apear in setup for notebook 1 and 4 to resolve compatibility issues with mediapipe.