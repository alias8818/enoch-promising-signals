# 2-bit KV cache with per-head residual scalars for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-per-head-residual-scalars-for-long-context-7b2ed59d8ee1`
Run ID: `2-bit-kv-cache-with-per-head-residual-scalars-for-long-context-7b2ed59d8ee1-20260608T180945346802+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a8aaff34ff66

## What looked useful

Across 108 measured rows, per-head gain consistently reduced attention-output relative L2 versus 2-bit per-token quantization, especially on heavy-tailed and outlier KV distributions; top-1 attention-logit match was unchanged and corrected output errors remained large.

## Boundaries and scale limits

No real transformer activations, no 7B model, no perplexity/retrieval metrics, no serving throughput measurement, and a strong per-token/head absmax quantization baseline with metadata costs not fully budgeted.

## Claim scope

Bounded NumPy mechanism probe on synthetic long-context-like KV tensors: per-head scalar gain reduces 2-bit KV reconstruction and attention-output magnitude error, but does not repair attention ranking or token-specific value loss.

## Why it stopped

Proxy synthetic mechanism probe found useful scalar-correction signal but insufficient fidelity for the long-context 2-bit KV-cache claim; this is not full validation.

## Recommended next action

Stop this run as no-paper proxy evidence; the next bounded test should use real GPT-2-small-class KV activation traces and task loss/retrieval metrics before any 7B-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate per-head scalar 2-bit KV correction on real GPT-2-small KV traces
- Success threshold: At the same metadata budget, scalar correction reduces loss degradation by at least 20% relative to the 2-bit baseline while preserving retrieval accuracy within 5 percentage points of FP32 on the tested context range.
- Stop condition: Stop if scalar correction changes reconstruction magnitude but fails to improve model loss/retrieval metrics versus the metadata-matched 2-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-residual-scalars-for-long-context-7b2ed59d8ee1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
