# Small-Transformer Anchor-Indexed KV Cache Evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-anchor-indexed-kv-cache-evaluation-3f4864c38c`
Run ID: `small-transformer-anchor-indexed-kv-cache-evaluation-3f4864c38c-20260518T061403537752+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aad9d2ebdfff

## What looked useful

Across three seeds, anchor-plus-recent preserved 99.87% answer accuracy at 25.83% mean allowed-cache fraction, while full attention reached 100.00% at 50.66%; recent-only reached 8.60%, and a similar-budget stride control reached 41.49%.

## Boundaries and scale limits

Synthetic task only; attention-mask evaluation rather than a production incremental KV-cache kernel; no pretrained LM, natural-language, long-context serving, or memory-bandwidth benchmark.

## Claim scope

In a 819k-parameter decoder-only transformer trained on a controlled synthetic anchor-retrieval task, retaining anchor-record tokens plus a recent window preserved retrieval answer accuracy while reducing the mean allowed-cache fraction relative to full attention.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal but remains synthetic and mask-based, so it is not paper-positive evidence.

## Recommended next action

Run a bounded pretrained small-LM follow-up with real incremental KV pruning on passkey retrieval and short natural-language continuation metrics before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Small-LM Anchor-Indexed KV Cache Validation
- Success threshold: Anchor-indexed cache retains retrieval accuracy within 2 percentage points of full KV at <=60% KV entries and beats same-budget non-semantic controls, with natural-language continuation NLL increase <=10%.
- Stop condition: Stop as negative if full KV succeeds but anchor-indexed cache loses more than 5 percentage points retrieval accuracy at <=60% KV entries or fails to beat same-budget controls.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-anchor-indexed-kv-cache-evaluation-3f4864c38c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
