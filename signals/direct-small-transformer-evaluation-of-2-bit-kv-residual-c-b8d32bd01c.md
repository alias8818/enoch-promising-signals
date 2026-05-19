# Direct small-transformer evaluation of 2-bit KV residual correction

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `98`
Project ID: `direct-small-transformer-evaluation-of-2-bit-kv-residual-c-b8d32bd01c`
Run ID: `direct-small-transformer-evaluation-of-2-bit-kv-residual-c-b8d32bd01c-20260514T115925646336+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c7106e4b8fcc

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct small-transformer evidence supports the residual-correction mechanism, but the implementation is conceptual rather than memory-optimized and lacks larger-model, multi-dataset, long-context, and serving-efficiency validation required for publication.

## Recommended next action

Run a bounded memory-accurate GPT-2-small-class follow-up with packed 2-bit KV plus residual metadata, using the same NLL recovery threshold and adding latency/bandwidth accounting; this Tier 1 result is mechanism-positive but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-accurate GPT-2-small-class validation of 2-bit KV residual correction
- Success threshold: Residual-corrected 2-bit KV recovers >=80% of plain-2bit mean-NLL degradation, stays within +0.10 mean NLL of fp16, and reduces effective KV memory versus fp16 under explicit byte accounting.
- Stop condition: Stop if the memory-accurate residual design fails to recover >=50% of plain-2bit degradation or cannot reduce effective KV memory versus fp16 on the first controlled dataset.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-transformer-evaluation-of-2-bit-kv-residual-c-b8d32bd01c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
