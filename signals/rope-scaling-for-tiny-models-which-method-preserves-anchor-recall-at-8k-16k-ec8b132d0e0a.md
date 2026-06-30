# RoPE Scaling for Tiny Models: Which Method Preserves Anchor Recall at 8k-16k?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rope-scaling-for-tiny-models-which-method-preserves-anchor-recall-at-8k-16k-ec8b132d0e0a`
Run ID: `rope-scaling-for-tiny-models-which-method-preserves-anchor-recall-at-8k-16k-ec8b132d0e0a-20260613T073930518640+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

The benchmark cleanly separated RoPE extension methods after the model reached 100% recall at the 1024-token training boundary: linear and dynamic NTK stayed at 1.0 accuracy through 16k, while unscaled RoPE and the naive ramp were near 8-class chance at 8k/16k.

## Boundaries and scale limits

Synthetic task only; start anchor only; 8 values; 48 eval samples per seed; 3 seeds; from-scratch tiny decoder; no pretrained LM, natural-language needle retrieval, randomized anchor positions, exact full YaRN implementation, or broader architecture sweep.

## Claim scope

In a synthetic 8-class start-anchor recall task with a 2-layer 128-wide RoPE decoder trained only at 128-1024 tokens, linear position interpolation and dynamic NTK scaling preserved recall at 8k and 16k across three seeds; no scaling and a naive YaRN-like ramp did not.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and start-anchor-only, not a broad validation of RoPE scaling for real tiny language models.

## Recommended next action

Run a bounded deepen test with randomized anchor positions and exact library implementations of linear, dynamic NTK, and YaRN on a pretrained or finetuned tiny LM before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized-anchor RoPE scaling benchmark for tiny pretrained LMs
- Success threshold: At least one scaling method exceeds unscaled RoPE by 30 percentage points or more at both 8k and 16k while maintaining at least 80% within-training-context recall.
- Stop condition: Stop if the model cannot reach at least 80% recall at the within-training-context control or if all scaling methods are within 10 percentage points of chance at 8k and 16k.

## Evidence references

- Artifact root: `<local-path>/projects/rope-scaling-for-tiny-models-which-method-preserves-anchor-recall-at-8k-16k-ec8b132d0e0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
