# Hash-Commit Gradient Aggregation for Untrusted CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-commit-gradient-aggregation-for-untrusted-cpu-workers-7e2993eb32b6`
Run ID: `hash-commit-gradient-aggregation-for-untrusted-cpu-workers-7e2993eb32b6-20260604T093418426381+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a224e97984d2

## What looked useful

Hash-commit aggregation is useful as a byte-integrity and audit primitive, not as a standalone trust mechanism for untrusted CPU gradient workers. In the final run, committed malicious gradients had 0% detection and 100% verification acceptance while shifting targeted aggregate coordinates by 1.0.

## Boundaries and scale limits

Synthetic float32 gradient vectors up to 5,000,000 dimensions, 8 workers, 2 malicious workers, local Python/Numpy implementation, no real distributed training or end-to-end model loss measurement.

## Claim scope

Local CPU simulation shows hash commitments over gradient bytes reliably detect post-commit mutation and stale-context replay, but do not detect malicious gradients that are committed and revealed consistently up front.

## Why it stopped

Proxy/local evidence is enough to falsify the standalone trust claim: hash commitments authenticate consistency with a prior byte string, not gradient correctness.

## Recommended next action

Stop this standalone commitment-only line; any next bounded test should add an independent semantic defense such as robust aggregation or redundant recomputation and compare against robust aggregation alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Plus Robust Aggregation Against Committed Gradient Poisoning
- Success threshold: The combined protocol must match robust aggregation's final loss within 2%, reject or bound at least 90% of committed poisoning influence under 25% malicious workers, and add less than 20% aggregation wall-clock overhead at the tested scale.
- Stop condition: Stop if committed malicious gradients remain accepted without reduced aggregate influence, or if hash/audit overhead exceeds 20% while providing no measurable benefit over robust aggregation alone.

## Evidence references

- Artifact root: `<local-path>/projects/hash-commit-gradient-aggregation-for-untrusted-cpu-workers-7e2993eb32b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
