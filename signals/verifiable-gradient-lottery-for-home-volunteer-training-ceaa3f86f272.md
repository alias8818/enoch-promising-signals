# Verifiable Gradient Lottery for Home-Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-gradient-lottery-for-home-volunteer-training-ceaa3f86f272`
Run ID: `verifiable-gradient-lottery-for-home-volunteer-training-ceaa3f86f272-20260518T080603104667+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/124efa13c452

## What looked useful

The mechanism is verifiable locally, but low-cost random auditing alone did not protect training from strong malicious gradients: 10%, 25%, and 50% audit collapsed accuracy near zero, while 75% audit recovered 0.961 mean accuracy versus 0.966 honest and full-verify baselines.

## Boundaries and scale limits

Tested only a CPU toy classification task, exact server recomputation, simple SHA-256 commitments, deterministic audit randomness, 10 seeds, 300 rounds, 32 selected workers per round, and simple sign-flip attacks; no home-network, privacy, incentive, Sybil, cryptographic proof, neural-network, LLM-scale, or multi-node evidence.

## Claim scope

On sklearn digits softmax regression with 30% malicious volunteers, a commit-then-random-audit gradient lottery detects malicious submissions in proportion to audit rate and preserves accuracy only when audit cost is high under a strong -5x sign-flip attack.

## Why it stopped

Proxy/local early falsification: the simple audit lottery alone needs about 75% recomputation in this toy strong-attack setting, so it is not a paper-ready low-cost volunteer-training defense.

## Recommended next action

Run a bounded deepen experiment adding norm clipping or robust aggregation and require honest-baseline accuracy within 1 percentage point at no more than 25% audit cost under the same 30% malicious -5x attack.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust Aggregation for Low-Cost Verifiable Gradient Lottery
- Success threshold: Mean test accuracy at least 0.956, within 1 percentage point of the 0.966 honest baseline from this run, with audit_cost_ratio no greater than 0.25 under the strong attack.
- Stop condition: Stop as negative if all robust variants either fall below 0.956 mean accuracy or require more than 0.25 audit cost on the same task and attack.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-gradient-lottery-for-home-volunteer-training-ceaa3f86f272`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
