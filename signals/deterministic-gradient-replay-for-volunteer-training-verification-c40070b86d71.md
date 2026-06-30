# Deterministic gradient replay for volunteer training verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-gradient-replay-for-volunteer-training-verification-c40070b86d71`
Run ID: `deterministic-gradient-replay-for-volunteer-training-verification-c40070b86d71-20260628T110715535003+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6807a94e26b3

## What looked useful

Deterministic gradient replay is mechanically viable when the verifier can exactly regenerate the data, initialization, batch schedule, and arithmetic path. The same evidence shows the approach is brittle to real-world determinism and data-access assumptions, so it is useful no-paper evidence rather than paper-positive validation.

## Boundaries and scale limits

Single-process Python standard-library CPU probe only: 192 synthetic samples, 10 features, 3 classes, 72 SGD steps, batch size 16. It does not test PyTorch/JAX kernels, GPU nondeterminism, mixed precision, dataloaders, distributed training, long trace storage, privacy-preserving commitments, or adversarial protocol security.

## Claim scope

In a toy deterministic CPU softmax trainer with fixed seed, generated dataset, fixed batch schedule, SGD, and SHA-256 commitments over quantized parameters and gradients, independent replay verifies a clean volunteer transcript and detects simple tampering of final weights, gradient hashes, batch order, and hidden label-flip training.

## Why it stopped

Closed as no-paper useful signal: the local probe supports the mechanism in a synthetic deterministic setting but does not provide direct evidence for real volunteer training verification.

## Recommended next action

Run a bounded PyTorch CPU/CUDA determinism follow-up on a small real model with deterministic flags, dataloader controls, and trace-size/runtime overhead measurement before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch deterministic gradient replay under framework and device controls
- Success threshold: Clean replay verifies bit-for-bit or within a declared quantized tolerance on every tested deterministic run; all planned tamper controls are rejected; verification overhead and trace bytes per step are reported.
- Stop condition: Stop if framework/device nondeterminism prevents repeat verification after deterministic settings are enabled, or if replay requires storing full gradients at a cost that makes small-model verification impractical.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-gradient-replay-for-volunteer-training-verification-c40070b86d71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
