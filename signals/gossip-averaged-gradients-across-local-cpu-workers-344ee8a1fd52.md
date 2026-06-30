# Gossip-Averaged Gradients Across Local CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaged-gradients-across-local-cpu-workers-344ee8a1fd52`
Run ID: `gossip-averaged-gradients-across-local-cpu-workers-344ee8a1fd52-20260604T041738600919+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Gossip averaging is useful for consensus and per-worker model quality: gossip_r4 reduced consensus MSE about 37x versus no communication and raised worker mean accuracy from about 0.831 to about 0.883, near all-reduce at about 0.888. It did not improve mean-model accuracy versus all-reduce or local training in this setup.

## Boundaries and scale limits

Synthetic convex-ish task only; 4 local CPU workers; no real neural network, real dataset, real network transport, larger worker topology, or large-scale training validation.

## Claim scope

On a synthetic non-IID 4-local-CPU-worker softmax-regression task, randomized pairwise gossip-averaged gradients reduce gradient communication error and model consensus drift as gossip rounds increase, and 4 rounds recover per-worker accuracy close to exact all-reduce.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports gossip as a consensus mechanism but does not show a practical mean-accuracy advantage over exact all-reduce or no-communication baselines.

## Recommended next action

Run a bounded real-dataset small-neural-model follow-up only if per-worker deployed models are the target; otherwise stop because the synthetic mean-model result does not justify a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset per-worker quality test for gossip-averaged gradients
- Success threshold: gossip_r4 per-worker mean accuracy within 1 percentage point of all-reduce, at least 3 percentage points above local no-communication, with consensus MSE at least 10x lower than local.
- Stop condition: Stop if gossip_r4 fails to beat local no-communication per-worker accuracy by 1 percentage point in at least 4 of 5 seeds or if communication overhead exceeds all-reduce wall time without a per-worker accuracy benefit.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaged-gradients-across-local-cpu-workers-344ee8a1fd52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
