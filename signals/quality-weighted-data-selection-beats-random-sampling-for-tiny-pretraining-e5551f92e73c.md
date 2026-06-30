# Quality-Weighted Data Selection Beats Random Sampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-weighted-data-selection-beats-random-sampling-for-tiny-pretraining-e5551f92e73c`
Run ID: `quality-weighted-data-selection-beats-random-sampling-for-tiny-pretraining-e5551f92e73c-20260610T222129984697+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/469411b4e18c

## What looked useful

Quality-weighted selection selected cleaner/higher-scored text and reduced mean clean validation loss from 2.72498 to 2.66563 (-0.05935, -2.18%) versus random; improvement appeared in all 5 seeds. A top-quality upper-bound selector reached 2.48501 mean loss, showing remaining headroom from stronger quality filtering.

## Boundaries and scale limits

Proxy-scale only: synthetic corruptions, tiny character-level transformer, 120k-character budget, 450 optimizer steps, clean WikiText-style validation, no natural web-quality scores, no subword/GPT-2-small-class model, no downstream transfer.

## Claim scope

In a controlled WikiText-2-derived contaminated corpus, heuristic quality-weighted selection of a fixed 120k-character pretraining budget improved clean held-out validation loss for a tiny character-level causal transformer versus uniform random selection across 5 seeds.

## Why it stopped

No-paper useful signal: the local controlled proxy supports the mechanism, but synthetic contamination and tiny character-level scale are insufficient for publication-grade evidence.

## Recommended next action

Run a medium confirmation on natural quality-scored text with a subword-tokenized tiny/GPT-2-small-class LM before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural quality-score confirmation for tiny LM data selection
- Success threshold: Quality-weighted sampling improves mean clean validation loss by at least 1% versus random, improves in at least 3 of 3 seeds, and the shuffled-score ablation removes most of the gain.
- Stop condition: Stop as unsupported if quality-weighted sampling fails to improve mean validation loss versus random or if the shuffled-score ablation performs similarly to true quality scores.

## Evidence references

- Artifact root: `<local-path>/projects/quality-weighted-data-selection-beats-random-sampling-for-tiny-pretraining-e5551f92e73c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
