# True fused-backward LOMO with int8 CPU-offloaded state on real-data GPT-2-small fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `true-fused-backward-lomo-with-int8-cpu-offloaded-state-on-eac4b5c821`
Run ID: `true-fused-backward-lomo-with-int8-cpu-offloaded-state-on-eac4b5c821-20260522T174504040627+0000`

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

- Parent run decision: LOMO-Plus: Gradient Clipping + 8-bit Offload: enoch://control-plane/projects/lomo-plus-gradient-clipping-8-bit-offload-62d3829c53b5/runs/lomo-plus-gradient-clipping-8-bit-offload-62d3829c53b5-20260522T171404920394+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93f4f84942ac

## What looked useful

Controlled run: int8 CPU LOMO state was 118.68 MB versus AdamW 474.70 MB (0.250x), CUDA peak allocation was 1156.44 MB versus 1279.54 MB (-123.10 MB), losses stayed finite, but throughput was 1319.49 tokens/s versus AdamW 3236.96 tokens/s (0.408x) and RSS final was higher.

## Boundaries and scale limits

Only 2-step smoke and 8-step controlled runs on Tiny Shakespeare real text with batch size 1 and sequence lengths 64/128. No validation perplexity, long-run convergence, larger corpus, larger batch, multi-GPU, or custom fused CUDA implementation was tested.

## Claim scope

Tier 1 GPT-2-small real-text fine-tuning mechanism test: a PyTorch backward-hook LOMO-style optimizer with int8 CPU-offloaded momentum state can execute finite in-backward updates and reduce optimizer-state storage versus AdamW, but the prototype is substantially slower.

## Why it stopped

Tier 1 direct test supports the memory mechanism but not a paper-positive optimizer: the PyTorch-hook int8 CPU-offloaded implementation is much slower than AdamW and convergence evidence is only a short finite-loss trace.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a medium GPT-2-small implementation test that reduces CPU offload overhead and measures validation perplexity over hundreds of steps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed-state medium GPT-2-small LOMO validation with perplexity and throughput threshold
- Success threshold: Candidate optimizer-state memory <= 0.30x AdamW, throughput >= 0.80x AdamW, validation perplexity within 5% of AdamW, and no retained nonzero full gradients after backward.
- Stop condition: Stop if throughput remains below 0.60x AdamW after packed-state implementation or validation perplexity is more than 10% worse than AdamW at matched tokens.

## Evidence references

- Artifact root: `<local-path>/projects/true-fused-backward-lomo-with-int8-cpu-offloaded-state-on-eac4b5c821`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
