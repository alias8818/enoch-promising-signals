# Residual-Aware Draft Head on a Small Real Transformer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6`
Run ID: `residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6-20260527T084803328421+0000`

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

- Parent run decision: Residual-Aware Draft for CPU Speculative Decoding: enoch://control-plane/projects/residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f/runs/residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f-20260525T115550958373+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a884e882bba0

## What looked useful

Across three seeds, the residual-aware delta head improved validation loss by 3.4856 +/- 0.0032 nats over the tied early head and by 2.8288 +/- 0.1769 nats over the learned direct vocabulary head. Final-model top-1 agreement improved by 0.0141 +/- 0.0018 over tied early and 0.0888 +/- 0.0124 over direct vocab. The residual-aware head used 589,824 trainable parameters versus 38,647,633 for the direct vocabulary head.

## Boundaries and scale limits

Only 128 train blocks and 48 validation blocks of length 64 were used; only one model, one layer, one dataset, and next-token draft metrics were tested. No speculative decoding acceptance-length, latency, layer sweep, larger model, or parameter-matched low-rank direct-head validation was run.

## Claim scope

On distilgpt2 layer 3 with Wikitext-2, a learned residual-stream delta before the frozen final layer norm and LM head improves intermediate draft next-token loss and final-model agreement over a tied early head and a naive learned direct vocabulary head in a small three-seed CPU test.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains a small-model, small-data local signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test with parameter-matched low-rank direct-head controls, a layer sweep, and speculative decoding acceptance-length metrics on distilgpt2 before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched residual-aware draft head with acceptance-length metrics
- Success threshold: Residual-aware head improves validation loss by at least 0.25 nats and mean accepted draft length or final-model top-1 agreement by at least 5% relative over the best parameter-matched direct control in at least two tested layers.
- Stop condition: Stop if a parameter-matched direct control matches residual-aware validation loss within 0.1 nats and matches or exceeds acceptance/agreement metrics in at least two tested layers.

## Evidence references

- Artifact root: `<local-path>/projects/residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
