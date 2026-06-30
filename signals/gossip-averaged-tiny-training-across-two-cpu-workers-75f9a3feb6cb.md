# Gossip-averaged tiny training across two CPU workers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gossip-averaged-tiny-training-across-two-cpu-workers-75f9a3feb6cb`
Run ID: `gossip-averaged-tiny-training-across-two-cpu-workers-75f9a3feb6cb-20260526T022911055046+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Best periodic gossip averaging matched centralized mean test accuracy across three seeds (0.97454) and improved over the average independent-worker accuracy by 2.15-3.47 percentage points per seed. Longer intervals (20-80 local steps) were better than averaging every step.

## Boundaries and scale limits

Synthetic data only; local multiprocessing pipes rather than real networked machines; three seeds; tiny MLP; no language-model, large-batch, WAN/LAN communication, fault-tolerance, or wall-clock scaling validation.

## Claim scope

On a synthetic non-IID four-class classification task with a tiny numpy MLP, two local CPU worker processes using periodic parameter averaging can match centralized SGD accuracy and outperform independently trained workers.

## Why it stopped

The local synthetic run supports the mechanism but is not paper-ready because it lacks real data and real distributed communication evidence.

## Recommended next action

Run a bounded deepen test on a real small dataset with actual two-host or socket-based worker communication and the same centralized, independent, one-shot, and periodic averaging controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-host gossip averaging on a real small dataset
- Success threshold: Periodic gossip reaches at least 98% of centralized test accuracy and exceeds the average independent-worker test accuracy by at least 1 percentage point in at least four of five seeds without more than 25% wall-clock overhead versus the matched centralized baseline.
- Stop condition: Stop if gossip fails to beat independent-worker controls in three of the first five seeds, or if communication overhead exceeds 50% before reaching 98% of centralized accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaged-tiny-training-across-two-cpu-workers-75f9a3feb6cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
