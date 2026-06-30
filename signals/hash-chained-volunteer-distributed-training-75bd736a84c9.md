# Hash-Chained Volunteer Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-volunteer-distributed-training-75bd736a84c9`
Run ID: `hash-chained-volunteer-distributed-training-75bd736a84c9-20260613T095811970300+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/274266e08693

## What looked useful

Hash chaining is useful as a transcript/audit layer, not as a standalone semantic guarantee for volunteer distributed training. Robust aggregation recovered the toy sign-flip attack, indicating the next useful layer is gradient robustness or verification.

## Boundaries and scale limits

Synthetic CPU-only logistic regression with 12 workers, 10 seeds, 50 rounds, and 32-dimensional gradients; no real volunteer identities, signatures, network faults, privacy constraints, large model, or datacenter-scale training was tested.

## Claim scope

In a deterministic synthetic logistic-regression volunteer training probe, per-worker hash-chained update records made transcript mutation and stale-model replay tamper-evident, but validly chained sign-flip updates still destroyed mean-aggregated model quality.

## Why it stopped

Proxy early falsification: hash chaining alone preserved transcript integrity but did not prevent harmful valid updates from collapsing mean-aggregated training quality.

## Recommended next action

Stop this run as no-paper evidence; the next bounded test should combine signed hash-chained records with explicit robust aggregation or gradient verification on a small neural workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed hash-chain plus robust aggregation on a small neural workload
- Success threshold: Across at least 5 seeds with 20-25% adversarial clients, robust hash-chained training stays within 3 percentage points of honest accuracy while detecting all transcript tampering/replay and keeping false rejection of honest workers below 5%.
- Stop condition: Stop if validly chained adversarial clients reduce robust training accuracy by more than 10 percentage points versus honest control or if transcript verification cannot reject replay/tampering without private state unavailable to verifiers.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-volunteer-distributed-training-75bd736a84c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
