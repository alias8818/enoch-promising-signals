# End-to-end residual-channel speculative decoding for GPT-2-small-class models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-residual-channel-speculative-decoding-for-gpt-2-f3f7758630`
Run ID: `end-to-end-residual-channel-speculative-decoding-for-gpt-2-f3f7758630-20260522T120412682023+0000`

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

- Parent run decision: Residual-channel speculative draft for tiny models: enoch://control-plane/projects/residual-channel-speculative-draft-for-tiny-models-2e023262e407/runs/residual-channel-speculative-draft-for-tiny-models-2e023262e407-20260522T114008478507+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

Later GPT-2 residual streams appear strong enough for residual-channel speculative drafting in a bounded direct test, but earlier block-6 residuals are too weak under held-out evaluation and practical speedup remains unmeasured.

## Boundaries and scale limits

Single seed, small held-out corpus, GPT-2-small only, no broad OpenWebText-style validation, no real block speculative decoder or KV-cache latency measurement, and block-6 residuals failed the 0.70 overlap threshold.

## Claim scope

Tier-1 GPT-2-small test: a compact residual adapter trained on block-9 hidden states can produce draft distributions with mean speculative acceptance overlap 0.7245 and target top-1 agreement 0.6567 on a Tiny Shakespeare held-out token split, improving over raw intermediate tied-head overlap 0.2806.

## Why it stopped

No-paper useful signal: Tier-1 mechanism support was observed for block 9, but this is not paper-positive without repeated seeds, broader corpora, a real latency implementation, and stronger draft-model baselines.

## Recommended next action

Run a bounded deepen follow-up implementing real K=4 speculative decoding latency for the block-9 residual adapter on broader held-out text with at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured K=4 latency for block-9 residual-channel speculative decoding
- Success threshold: Mean acceptance overlap >= 0.70 and measured end-to-end decoding speedup > 1.15x with no increase in target-distribution NLL beyond 0.05 on the held-out set.
- Stop condition: Stop if mean acceptance overlap is < 0.70 in at least two of three seeds or if measured end-to-end speedup is <= 1.15x after verifier overhead.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-residual-channel-speculative-decoding-for-gpt-2-f3f7758630`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
