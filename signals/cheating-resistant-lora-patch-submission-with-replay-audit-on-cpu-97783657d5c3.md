# Cheating-Resistant LoRA Patch Submission with Replay Audit on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-lora-patch-submission-with-replay-audit-on-cpu-97783657d5c3`
Run ID: `cheating-resistant-lora-patch-submission-with-replay-audit-on-cpu-97783657d5c3-20260621T155542356977+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14bbe7f1f354

## What looked useful

Replay audit is useful as a reproducibility and claimed-metric verifier, not as a standalone cheating-resistance mechanism. A policy/data-access layer is required for replayable but forbidden training recipes.

## Boundaries and scale limits

Tested only a small linear-regression LoRA proxy: 24 trials, dim=16, rank=4, train_n=96, eval_n=64, steps=90, single-process CPU. Not tested on transformer LoRA, GPU nondeterminism, hidden leaderboards, cryptographic transcript commitments, collusion, or large-scale replay economics.

## Claim scope

Toy CPU synthetic-regression LoRA replay audit: deterministic replay catches metric, patch, and seed forgeries when submissions diverge from the declared recipe, but replay-only does not reject truthfully replayable policy violations.

## Why it stopped

Proxy evidence is sufficient to reject replay-only as a complete cheating-resistant mechanism, but it is not direct transformer-scale evidence for a paper.

## Recommended next action

Run a bounded real-model deepen test using a tiny or GPT-2-small-class LoRA setup with deterministic CPU replay, corrupt submissions, and a hidden-holdout/policy gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model deterministic LoRA replay audit with hidden-holdout policy gate
- Success threshold: Honest submissions accepted at 100%; non-replayable forgeries rejected at 100%; replayable policy violations rejected only when the policy or hidden-holdout gate is enabled; replay cost reported and bounded.
- Stop condition: Stop if deterministic real-model replay cannot be made reproducible on CPU within a bounded run, or if honest submissions are rejected before attack tests.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-lora-patch-submission-with-replay-audit-on-cpu-97783657d5c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
