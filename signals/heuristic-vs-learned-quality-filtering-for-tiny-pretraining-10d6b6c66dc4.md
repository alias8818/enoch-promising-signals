# Heuristic vs Learned Quality Filtering for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heuristic-vs-learned-quality-filtering-for-tiny-pretraining-10d6b6c66dc4`
Run ID: `heuristic-vs-learned-quality-filtering-for-tiny-pretraining-10d6b6c66dc4-20260613T155243132078+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c652a0ea698

## What looked useful

Across four seeds, learned filtering beat heuristic filtering on clean held-out LM loss by mean delta -0.3173 and beat random selection by mean delta -0.5423; learned selection averaged 0.963 clean-label fraction versus 0.404 for the heuristic.

## Boundaries and scale limits

Synthetic documents, synthetic labels, character-level tokenizer, tiny Transformer, 260 steps per condition, and no real web corpus or GPT-2-small-class validation.

## Claim scope

In a synthetic mixed-quality document pool, a learned quality classifier selected a much cleaner fixed-size corpus than a hand-built heuristic and produced lower held-out clean-text loss for a tiny character Transformer across four seeds.

## Why it stopped

Closed as no-paper useful signal because the result is a synthetic proxy, not direct publication-grade evidence for real tiny pretraining.

## Recommended next action

Run a bounded real-corpus follow-up using a standard tokenizer and parameter-matched small decoder on a held-out clean validation domain before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus learned vs heuristic filtering for tiny decoder pretraining
- Success threshold: Learned filtering must beat heuristic filtering on mean held-out validation loss by at least 5% relative perplexity across at least three seeds without reducing selected-token diversity by more than 20%.
- Stop condition: Stop if the learned filter does not beat the heuristic in at least two of three seeds or if gains vanish after controlling for selected-token length/diversity.

## Evidence references

- Artifact root: `<local-path>/projects/heuristic-vs-learned-quality-filtering-for-tiny-pretraining-10d6b6c66dc4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
