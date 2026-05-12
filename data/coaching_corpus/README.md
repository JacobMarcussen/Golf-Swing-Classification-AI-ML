# Coaching corpus templates

Sixteen documents covering the 8 GolfDB swing positions (Address, Toe-up, Mid-backswing, Top, Mid-downswing, Impact, Mid-followthrough, Finish). Two documents per position:

- **`*_form.md`** — what the position looks like and what good form involves
- **`*_faults.md`** — common faults at this position, the deviation pattern that signals each, and what the golfer should work on to fix it

## Writing guidelines

**Use natural golf-coaching language.** The agent will retrieve from these documents based on semantic similarity to deviation summaries. Words and phrases that should appear naturally in the documents:

- Joint names: spine angle, hip rotation, shoulder turn, wrist hinge, elbow flex, knee flex
- Body axes: vertical, horizontal, target line, swing plane
- Common fault names: early extension, casting, over-the-top, sway, slide, chicken wing, scooping, lifting

**Keep claims biomechanical, not stylistic.** Different pros have different swings. Frame things as "typical pros do X" or "the most common range is Y" rather than "you must do X." Acknowledge style variation.

**Use specific numbers where possible.** "Spine angle from vertical typically 35-45°" is more useful than "tilted forward."

**Each document: 250-500 words.** Concise. The agent retrieves chunks of these so density of useful information matters more than length.

**Tone: factual, neutral, like a coaching textbook.** Not promotional, not condescending.

## How to fill in a template

Each template file has section headers and bracketed prompts. Replace the bracketed text with your content. Don't leave placeholders unfilled.

## Distribution

Team of 4: one person takes 4 documents = ~1 hour each. Or split by position: each person takes 2 P-positions (form + faults each) = 4 documents.

## After writing

Save all 16 files in `data/coaching_corpus/` in your project directory. The phase 4b notebook will read from there.
