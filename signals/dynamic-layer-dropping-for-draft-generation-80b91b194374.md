# Dynamic Layer Dropping for Draft Generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-layer-dropping-for-draft-generation-80b91b194374`
Run ID: `dynamic-layer-dropping-for-draft-generation-80b91b194374-20260530T003413479287+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/766a0e159b49

## What looked useful

Dynamic layer dropping is mechanically plausible as a draft-generation strategy if shallow prefixes are explicitly trained; naive layer dropping without auxiliary losses failed badly in this setup.

## Boundaries and scale limits

Synthetic data, small transformer, greedy-token agreement proxy only; no pretrained LLM, no real speculative decoding verifier loop, no wall-clock serving speedup demonstrated because the benchmarked toy forward passes are overhead dominated.

## Claim scope

On a 1.2M-parameter, 6-layer synthetic next-token transformer, confidence-gated shallow-prefix drafting reached 99.68% agreement with the full-depth greedy token while using 49.3% of full layers on average, but only when auxiliary shallow losses were used.

## Why it stopped

No-paper closure: this is a useful synthetic proxy signal with a negative control, not full validation of large-model draft generation.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class model with real text and an actual speculative decoding acceptance/speed benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Auxiliary-Trained Layer-Dropped Drafting on GPT-2-Small-Class Text
- Success threshold: At least 95% verifier acceptance with at least 1.2x end-to-end draft-generation throughput improvement versus full-depth drafting, without worse validation perplexity than the dense baseline by more than 2%.
- Stop condition: Stop if auxiliary shallow drafting cannot exceed 90% acceptance or if measured end-to-end throughput is not better than full-depth drafting after overhead-aware batching.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-layer-dropping-for-draft-generation-80b91b194374`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
