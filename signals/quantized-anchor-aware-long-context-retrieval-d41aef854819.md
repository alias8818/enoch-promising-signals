# Quantized Anchor-Aware Long Context Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-anchor-aware-long-context-retrieval-d41aef854819`
Run ID: `quantized-anchor-aware-long-context-retrieval-d41aef854819-20260527T155413675519+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

Anchor-aware mixed precision can help when quantization error contributes to retrieval misses: in the stress probe, anchor-mixed int4 improved top-1 over uniform int4 by +0.012 to +0.038 and matched fp32 top-1 at 0.57 versus 0.50 bytes/token-equivalent. The effect was not consistent in the easier probe, so the mechanism is conditional rather than broadly validated.

## Boundaries and scale limits

No transformer was trained or evaluated; no real text corpus, generation metric, production KV-cache kernel, latency benchmark, or matched end-to-end LLM memory budget was tested. Evidence is a CPU-only synthetic proxy with 240 trials per context setting.

## Claim scope

Paired synthetic dot-product KV retrieval with rare known anchor keys: preserving 2% anchor keys at fp32 while quantizing all other keys to int4 recovered fp32 top-1 accuracy in a collision-prone stress probe at 4k-32k context lengths, but showed mixed benefit in an easier probe.

## Why it stopped

Closed as no-paper useful signal: this run produced a reproducible synthetic mechanism probe, but it is proxy-only and insufficient for a publication-grade long-context retrieval claim.

## Recommended next action

Run a bounded direct-evidence transformer KV-cache follow-up on Needle-in-a-Haystack or a small LongBench subset, comparing uniform int4, random mixed precision, and anchor-aware mixed precision under matched memory and latency reporting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer KV-cache anchor-aware quantization on needle retrieval
- Success threshold: Anchor-aware mixed precision improves retrieval accuracy by at least 3 percentage points over uniform int4 and random mixed precision at <=1.15x int4 KV memory, without more than 10% latency regression on the tested model/context setting.
- Stop condition: Stop if anchor-aware mixed precision fails to beat both uniform int4 and random mixed precision by at least 1 percentage point in two independently seeded direct transformer runs, or if the implementation overhead exceeds the 1.15x memory target before accuracy improves.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-anchor-aware-long-context-retrieval-d41aef854819`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
