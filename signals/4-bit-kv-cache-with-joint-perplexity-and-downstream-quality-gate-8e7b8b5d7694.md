# 4-bit KV Cache with Joint Perplexity and Downstream Quality Gate

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-kv-cache-with-joint-perplexity-and-downstream-quality-gate-8e7b8b5d7694`
Run ID: `4-bit-kv-cache-with-joint-perplexity-and-downstream-quality-gate-8e7b8b5d7694-20260628T103004010182+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92970d39d153

## What looked useful

4-bit simulated KV-cache error passed the joint quality gate on two GPT-2 bounded runs: short NLL delta -0.002491 with MC delta 0.0, and longer-context NLL delta +0.004903 with MC delta 0.0. A 2-bit longer-context control failed with NLL delta +1.219436 and MC delta -0.5, showing the gate can reject damaging cache precision.

## Boundaries and scale limits

No packed int4 cache backend, no measured real KV memory savings, no throughput claim, no 7B+ model, no broad benchmark suite, and only hundreds of likelihood tokens plus a small local downstream gate.

## Claim scope

On GPT-2 small-class CUDA inference with local held-out text and continuation-choice probes, per-token/per-head-vector 4-bit KV-cache quantize/dequantize simulation preserved NLL/perplexity and downstream MC accuracy within the predeclared joint gate; a matched 2-bit control failed the same gate.

## Why it stopped

The result is a bounded quality simulation, not a full validation of deployable 4-bit KV-cache memory or serving performance.

## Recommended next action

Stop this worker run as no-paper useful signal; next implement a real packed 4-bit KV-cache backend and rerun the same joint gate plus measured memory/tokens-per-second before any larger model campaign.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed 4-bit KV-cache backend with joint quality and throughput gate
- Success threshold: NLL delta <= 0.05, downstream MC accuracy delta >= -0.05, measured KV-cache memory reduction >= 3.5x, and decode tokens-per-second no worse than 20% below FP16/BF16 baseline on the same hardware.
- Stop condition: Stop if packed-cache implementation cannot demonstrate measured memory reduction, if the joint quality gate fails, or if decode throughput regresses by more than 20% after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-with-joint-perplexity-and-downstream-quality-gate-8e7b8b5d7694`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
