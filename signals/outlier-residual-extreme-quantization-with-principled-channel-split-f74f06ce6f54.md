# Outlier-Residual Extreme Quantization with Principled Channel Split

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-residual-extreme-quantization-with-principled-channel-split-f74f06ce6f54`
Run ID: `outlier-residual-extreme-quantization-with-principled-channel-split-f74f06ce6f54-20260516T175312593243+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78b0bfec3762

## What looked useful

Residual channel preservation is useful versus no split/random in layer reconstruction, and the activation-weight score gave the best small downstream 3-bit held-out loss, but the evidence is mixed because 2-bit worsened and reconstruction was essentially tied/slightly worse than weight-norm.

## Boundaries and scale limits

Tested only distilgpt2, Wikitext-2 validation slices, one seed, 6,398 downstream eval tokens, simple dequantized PyTorch matmul, no packed kernel, no larger model, no multi-dataset robustness, and no throughput claim.

## Claim scope

Bounded local distilgpt2/Wikitext-2 evidence: activation-weight residual channel splitting improved downstream held-out loss for 3-bit weight-only quantization with 2-5% residual channels, but did not improve 2-bit downstream loss and did not beat weight-norm splitting on layer reconstruction.

## Why it stopped

No-paper mixed result: this is a bounded proxy plus small downstream validation, not a full validation; the 2-bit extreme setting is early-falsified under this implementation, while the 3-bit signal needs robustness before any paper claim.

## Recommended next action

Run one bounded deepen follow-up on GPT-2-small-class or a larger held-out Wikitext/OpenWebText slice with 3-bit quantization, multiple seeds, and matched effective-bit comparisons against weight-norm and random residual splits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust 3-bit activation-weight residual split validation
- Success threshold: Principled 3-bit residual split reduces delta loss vs FP16 by at least 10% relative to the best non-oracle baseline and beats weight-norm on at least two of three seeds/splits without hurting any tested layer family catastrophically.
- Stop condition: Stop as negative if principled selection is tied with or worse than weight-norm/random on average downstream loss, or if the gain appears only on one split/seed.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-residual-extreme-quantization-with-principled-channel-split-f74f06ce6f54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
