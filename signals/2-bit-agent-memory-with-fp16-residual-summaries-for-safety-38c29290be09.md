# 2-bit Agent Memory with FP16 Residual Summaries for Safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-agent-memory-with-fp16-residual-summaries-for-safety-38c29290be09`
Run ID: `2-bit-agent-memory-with-fp16-residual-summaries-for-safety-38c29290be09-20260608T075737371442+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e2b1eb0a4bf6

## What looked useful

2-bit memory substantially damaged safety-critical retrieval in the synthetic paired stress test. A 16-coefficient FP16 residual summary consistently recovered about 4.6 to 5.3 percentage points exact unsafe top-1 recall and about 2.4 to 2.7 points top-10 recall over plain 2-bit, while doubling storage from 256 to 512 bits per memory and remaining far below dense FP16 recall near 99%.

## Boundaries and scale limits

No real text embeddings, learned residual basis, long-horizon agent memory updates, downstream policy behavior, GPT-2-class model integration, or datacenter-scale validation were tested.

## Claim scope

Synthetic paired safe/unsafe vector-memory retrieval with 128-dimensional memories, per-vector 2-bit quantization, and known FP16 residual subspaces up to 16 coefficients.

## Why it stopped

The result is a synthetic proxy mechanism test: it supports a modest residual-summary benefit but is not direct/full validation of agent safety memory.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a real embedding-memory benchmark with learned residual bases and matched-budget int8/product-quantization controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned FP16 residual summaries for safety-labeled text memory retrieval
- Success threshold: At matched memory budget, 2-bit plus learned residual summaries improves safety top-1 recall by at least 5 absolute percentage points over the strongest non-residual compressed baseline and does not increase false safe-neighbor top-1 errors.
- Stop condition: Stop if learned residual summaries fail to beat the strongest matched-budget compressed baseline by 2 absolute top-1 recall points on two independent seeds or if gains require more storage than int8 for worse safety recall.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-agent-memory-with-fp16-residual-summaries-for-safety-38c29290be09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
