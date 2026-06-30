# Real-model exact-anchor KV snapshot validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-exact-anchor-kv-snapshot-validation-5c92405e0b`
Run ID: `real-model-exact-anchor-kv-snapshot-validation-5c92405e0b-20260530T023001018797+0000`

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

- Parent run decision: Exact-Anchor KV Snapshots for Long Context: enoch://control-plane/projects/exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe/runs/exact-anchor-kv-snapshots-for-long-context-15cb0f71abbe-20260529T223423529558+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Exact-anchor KV snapshot resume is functionally exact within float32 tolerance for the tested real pretrained decoder-only models; 26/26 comparisons passed and deliberately corrupted snapshots produced much larger logit errors.

## Boundaries and scale limits

Only two GPT-2-family Hugging Face causal LMs, float32 CPU inference, short prompts of 14-22 tokens, anchors 4-16, no serialization boundary, no quantized/mixed-precision cache, no GPU kernels, no serving concurrency, and no non-GPT architecture coverage.

## Claim scope

Tier 1 direct CPU validation: cloned KV-cache anchor snapshots for distilgpt2 and gpt2 reproduce per-sequence full-recompute suffix logits within torch allclose rtol=1e-5, atol=1e-5 across 26 natural-language prompt/anchor comparisons, with corruption controls showing sensitivity to wrong snapshots.

## Why it stopped

Tier 1 direct validation succeeded mechanistically but remains too narrow for publication readiness; this is not a negative mechanism result, but it is finalized negative at the paper gate.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a deeper direct validation across modern Cache APIs, one Llama-like architecture, serialization round trips, and longer contexts before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-architecture and serialized exact-anchor KV snapshot validation
- Success threshold: At least 99/100 prompt-anchor comparisons pass torch.allclose(rtol=1e-5, atol=1e-5), no uncorrupted max_abs_diff exceeds 1e-3, and every corrupted-cache control exceeds the corresponding uncorrupted max_abs_diff by at least 10x.
- Stop condition: Stop as negative or mixed if any architecture has repeated uncorrupted allclose failures after position ids and attention masks are verified, or if serialization changes logits above 1e-3 max_abs_diff.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-exact-anchor-kv-snapshot-validation-5c92405e0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
