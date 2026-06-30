# Adaptive Draft Length via Acceptance Prediction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-draft-length-via-acceptance-prediction-fd0293dfc97c`
Run ID: `adaptive-draft-length-via-acceptance-prediction-fd0293dfc97c-20260607T005434670431+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ef1d873df424

## What looked useful

Acceptance prediction appears useful for adaptive draft length when predictor AUC is around 0.67 to 0.68; when AUC falls near 0.55, adaptive gains collapse to roughly 0.1% to 0.4%, leaving most oracle headroom unused.

## Boundaries and scale limits

Proxy-only synthetic traces; no real draft/target model logits, no wall-clock serving latency, no KV-cache or verifier-kernel effects, no tokenizer/prompt diversity, and no 7B-class or production-scale validation.

## Claim scope

In a reproducible synthetic speculative-decoding acceptance simulator with confidence-like predictive features, choosing draft length by predicted expected tokens per cost improved simulated tokens-per-cost over the best fixed K by about 2.6% to 2.8% in predictive IID and mild-shift scenarios at draft_cost=0.12, with near-zero benefit in low-signal traces.

## Why it stopped

No-paper useful signal: this run provides synthetic mechanism evidence only, not direct full validation on real models or serving latency.

## Recommended next action

Run a bounded real-model speculative decoding benchmark with a small draft/target pair, logging acceptance features, chosen K, fixed-K controls, and actual tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model acceptance-predicted adaptive draft length benchmark
- Success threshold: Adaptive-K improves measured tokens/sec by at least 2% over the best fixed K on the same prompt set in at least two generation settings, with no quality or correctness regression under standard speculative decoding acceptance.
- Stop condition: Stop if predictor AUC is below 0.60 or adaptive-K fails to beat the best fixed K by 1% in an initial real-model benchmark of at least 500 generated sequences.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-draft-length-via-acceptance-prediction-fd0293dfc97c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
