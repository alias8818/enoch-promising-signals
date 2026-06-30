# Held-Out Probe Tasks as Proof-of-Contribution in Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-probe-tasks-as-proof-of-contribution-in-volunteer-cpu-training-7bf76ee6d703`
Run ID: `held-out-probe-tasks-as-proof-of-contribution-in-volunteer-cpu-training-7bf76ee6d703-20260621T094937282113+0000`

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

Held-out probes are useful as a statistical quality gate for update utility, not as standalone proof-of-contribution. At a threshold accepting 95% of useful updates, trivial spoofing had 0% accept rate, but surrogate training had 100% accept rate, yielding a 40% overall false accept rate among not-assigned-data submissions.

## Boundaries and scale limits

CPU-only synthetic convex model; no real neural network, no multi-round volunteer protocol, no adaptive probe leakage attack, no heterogeneous hardware, and no cryptographic CPU-cycle proof.

## Claim scope

In a 40-seed synthetic logistic-regression proxy with 320 worker submissions, secret held-out probe loss improvement rejects lazy, claimed-only, and random-update submissions, but it does not prove assigned volunteer CPU training because same-distribution and shifted-distribution surrogate training pass the probe gate.

## Why it stopped

Proxy early falsification of the strong proof claim: hidden probes measured useful target-distribution improvement but could not distinguish assigned CPU training from surrogate training.

## Recommended next action

Stop this run as proxy evidence: do not claim proof-of-contribution; run a bounded medium follow-up on a small neural-network task with adaptive surrogate attackers if further evidence is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium neural-network probe gate with surrogate and probe-leakage attackers
- Success threshold: At 95% honest update acceptance, trivial spoofing false accept rate below 5%, surrogate/adaptive attacker false accept rate measured explicitly, and no more than 5% relative degradation in accepted-update validation loss versus accepting all honest updates.
- Stop condition: Stop if surrogate or probe-leakage attackers exceed 50% false accept rate at the 95% honest-acceptance threshold, because the protocol remains a utility gate rather than proof-of-contribution.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-probe-tasks-as-proof-of-contribution-in-volunteer-cpu-training-7bf76ee6d703`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
