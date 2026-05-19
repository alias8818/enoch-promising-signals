# Residual-Channel 2-Bit GPT-2 Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-2-bit-gpt-2-small-pretraining-36993888df3a`
Run ID: `residual-channel-2-bit-gpt-2-small-pretraining-36993888df3a-20260515T023937069945+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/08a94314b5ab

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy evidence showed residual-channel 2-bit recovered a small amount of loss versus pure 2-bit but remained worse than dense, slower, and dependent on extra full-precision parameters; this is not full GPT-2-small validation.

## Recommended next action

Stop this run as a proxy early falsification of the GPT-2-small pretraining claim; only pursue a bounded deepen follow-up if it uses parameter-matched controls and production-like 2-bit kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-Matched Residual-Channel 2-Bit GPT Proxy With Packed Kernels
- Success threshold: Residual-channel 2-bit reaches within 1% validation loss or perplexity of dense while reducing effective model memory or improving throughput, and beats pure 2-bit by a statistically persistent margin.
- Stop condition: Stop if parameter-matched residual-channel 2-bit remains more than 2% worse than dense validation loss, fails to beat pure 2-bit across seeds, or provides no measured memory/throughput advantage with packed kernels.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-2-bit-gpt-2-small-pretraining-36993888df3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
