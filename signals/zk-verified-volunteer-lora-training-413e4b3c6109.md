# ZK-Verified Volunteer LoRA Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zk-verified-volunteer-lora-training-413e4b3c6109`
Run ID: `zk-verified-volunteer-lora-training-413e4b3c6109-20260628T092007698499+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9dde20d17e26

## What looked useful

Rank-only algebraic verification caught malformed tampering but accepted all algebraically valid malicious updates in the seeded toy run; adding a public canary-loss gate rejected 92.9% of malicious submissions and reduced final test MSE from 8.1348 to 0.4549.

## Boundaries and scale limits

No real ZK proof backend, no privacy proof, no transformer or GPT-2-small-class LoRA training, no volunteer network, no proof cost benchmark, and no multi-seed robustness sweep.

## Claim scope

Toy synthetic linear-regression LoRA aggregation with exact integer low-rank proof objects, finite-field Freivalds consistency checks, 16 clients per round, 8 rounds, and 35% adversarial submissions.

## Why it stopped

Closed as no-paper useful signal because this was a toy/proxy mechanism test, not a full ZK-private volunteer LoRA validation.

## Recommended next action

Deepen with a real small proof backend or exact arithmetic circuit for one LoRA training step and measure proof cost plus robustness on a small transformer before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Circuit-backed small LoRA update verification with semantic anti-poison checks
- Success threshold: Reject at least 90% of tested harmful submissions while preserving at least 95% honest-update acceptance and keeping verifier overhead below the simulated training-step cost for the chosen small model.
- Stop condition: Stop if semantic constraints cannot be represented in the proof/circuit without exceeding local memory/time limits or if poison rejection is not materially better than rank-only verification.

## Evidence references

- Artifact root: `<local-path>/projects/zk-verified-volunteer-lora-training-413e4b3c6109`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
