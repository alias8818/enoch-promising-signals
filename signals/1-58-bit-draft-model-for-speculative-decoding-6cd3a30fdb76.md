# 1.58-bit Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-58-bit-draft-model-for-speculative-decoding-6cd3a30fdb76`
Run ID: `1-58-bit-draft-model-for-speculative-decoding-6cd3a30fdb76-20260602T182701493241+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

Across seeds 7-11, the ternary draft averaged 3.878 accepted tokens per gamma=5 block versus 3.733 for dense, a +0.145 accepted-token delta and 1.039x token-acceptance ratio, while using a 0.145 storage-bit proxy ratio versus FP16 dense weights.

## Boundaries and scale limits

Synthetic oracle target, 64-token vocabulary, 4-token context, MLP drafts, no real LLM target, no production ternary kernels, and speedup measured only as an accepted-token/target-call proxy.

## Claim scope

In a controlled synthetic autoregressive oracle setting with MLP draft models, a ternary 1.58-bit-style draft preserved enough target-distribution fidelity for speculative decoding and improved acceptance versus a matched dense draft across five seeds.

## Why it stopped

No-paper closure: this run produced a useful controlled mechanism signal, but it is synthetic/toy-scale proxy evidence rather than full LLM speculative-decoding validation.

## Recommended next action

Run a bounded GPT-2-small-class deepen experiment with a real pretrained target, parameter-matched dense and ternary draft models, exact speculative acceptance, and measured end-to-end throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class ternary draft speculative decoding validation
- Success threshold: Ternary draft achieves at least 95% of dense-draft acceptance at matched parameter scale, improves accepted tokens per draft-byte by at least 2x, and does not reduce end-to-end speculative throughput versus dense draft on the tested GPU.
- Stop condition: Stop if ternary acceptance is below 90% of dense in two independent runs or if kernel/runtime overhead eliminates any accepted-token-per-second benefit despite storage savings.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-draft-model-for-speculative-decoding-6cd3a30fdb76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
