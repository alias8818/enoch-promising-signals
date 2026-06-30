# CPU gradient audit swarm for volunteer DDP training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-gradient-audit-swarm-for-volunteer-ddp-training-dbed02076d79`
Run ID: `cpu-gradient-audit-swarm-for-volunteer-ddp-training-dbed02076d79-20260621T070312168953+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

CPU spot recomputation is a plausible integrity check for large non-stealthy volunteer gradient corruption when the coordinator can reproduce assigned minibatch gradients. The same setup misses perturbations below audit tolerance, so robustness depends on tolerance policy and longer-horizon adversarial testing.

## Boundaries and scale limits

No live PyTorch DDP/Gloo/NCCL transport, no all-reduce integration, no real volunteer network, no privacy/Sybil model, no adaptive adversary, and no large-model training. The result tests the audit mechanism only.

## Claim scope

In a toy NumPy CPU simulation of volunteer gradient submission, random coordinator-side spot recomputation plus quarantine detected audited sign-flip gradients and reduced aggregate-gradient relative error from 0.6517 with no audit to 0.0483 at 25% audit and 0.0266 at 50% audit over 8 workers, 40 rounds, and 10 trials.

## Why it stopped

Proxy simulation produced a useful mechanism signal but is not direct DDP evidence or paper-ready validation.

## Recommended next action

Run a bounded live PyTorch CPU DDP/Gloo follow-up that implements the same audit/quarantine policy and reports detection, aggregate-gradient error, and throughput overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live CPU DDP/Gloo gradient audit with quarantine
- Success threshold: 25% audit reduces sign-flip aggregate-gradient relative error by at least 80% versus no audit, detects at least 95% of audited sign-flip corruptions, has zero false positives under honest controls, and adds less than 35% wall-clock overhead versus no audit.
- Stop condition: Stop as negative if deterministic recomputation cannot match honest worker gradients within tolerance, false positives occur in honest controls, or 25% audit fails to reduce sign-flip aggregate error by at least 50%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-gradient-audit-swarm-for-volunteer-ddp-training-dbed02076d79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
