# Blockwise 8-bit Adam on CPU-only GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adam-on-cpu-only-gpt-2-small-pretraining-205199c4646a`
Run ID: `blockwise-8-bit-adam-on-cpu-only-gpt-2-small-pretraining-205199c4646a-20260628T145222282653+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3118b0c19190

## What looked useful

Blockwise 8-bit state reduces estimated GPT-2-small Adam optimizer memory from 949.40 MiB to about 237.6 MiB, but the tested naive absmax and min/max quantizers diverged in closed-loop optimization and were 2.83x-3.16x slower per update in NumPy.

## Boundaries and scale limits

No PyTorch/Transformers GPT-2 training loop was available in the Python 3.14 environment. Evidence is optimizer-mechanism and proxy convergence only, with 4M sampled GPT-2-shaped elements rather than a full language-model training run.

## Claim scope

A NumPy CPU proxy tested naive blockwise 8-bit Adam state quantization on GPT-2-small-shaped tensors, sampled optimizer updates, and deterministic convex closed-loop convergence controls. It did not test full GPT-2-small pretraining.

## Why it stopped

Early proxy falsification: the tested naive blockwise 8-bit Adam variants diverged in deterministic closed-loop optimization despite good one-step update cosine, so full CPU-only GPT-2-small pretraining is not justified from this implementation.

## Recommended next action

Stop this run as a no-paper proxy falsification; only revisit after implementing a stability-aware 8-bit Adam design and testing it first on the same closed-loop control before any GPT-2-small CPU pretraining attempt.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stability-aware 8-bit Adam control test before CPU GPT-2 pretraining
- Success threshold: Pass the closed-loop control at lr=1e-3 and lr=1e-4, keep optimizer state at least 70% smaller than FP32 Adam, and avoid more than 2x CPU update overhead in a vectorized implementation.
- Stop condition: Stop if the stabilized optimizer diverges in the convex control or requires learning rates below 1e-5 to remain finite.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-on-cpu-only-gpt-2-small-pretraining-205199c4646a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
