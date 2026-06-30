# Small-verifier quality-filtered pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-verifier-quality-filtered-pretraining-cd4e027a83d4`
Run ID: `small-verifier-quality-filtered-pretraining-cd4e027a83d4-20260629T203331647248+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

Across 3 seeds, the verifier achieved mean held-out AUC 0.978 and selected a top quartile with 88.0% true high-quality documents. Verifier-filtered pretraining reduced clean validation loss from 0.2737 to 0.2132, a 22.1% relative reduction versus unfiltered, while oracle-high reached 0.1965 and verifier-bottom worsened to 4.1768.

## Boundaries and scale limits

Synthetic corpus only; tiny character-level GRU only; 3 seeds; no real web text, GPT-2-small-class transformer, downstream transfer, or large-scale token budget validation.

## Claim scope

In a controlled synthetic noisy-corpus setup, a small learned verifier trained on limited quality labels can select documents that improve equal-token tiny character-LM clean validation loss versus unfiltered pretraining.

## Why it stopped

Stopped after a reproducible synthetic useful signal; this is not paper-positive because the evidence is toy/synthetic and does not directly validate real-corpus or transformer pretraining behavior.

## Recommended next action

Run a bounded real-corpus deepen experiment using a small transformer, trusted quality labels or heuristics, equal-token controls, and clean held-out plus downstream metrics before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-transformer test of verifier-filtered pretraining
- Success threshold: Verifier-filtered pretraining beats unfiltered by at least 3% relative clean held-out loss or a statistically consistent downstream improvement across seeds, while bottom-ranked data is worse and oracle/heuristic-high is directionally best.
- Stop condition: Stop as unsupported if verifier-filtered does not beat unfiltered on clean held-out loss in at least 2 of 3 seeds or if gains disappear when token budget and document count are controlled.

## Evidence references

- Artifact root: `<local-path>/projects/small-verifier-quality-filtered-pretraining-cd4e027a83d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
