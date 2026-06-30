# Gossip-Averaged Gradients for Two-Node CPU Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `gossip-averaged-gradients-for-two-node-cpu-training-6019b43ec793`
Run ID: `gossip-averaged-gradients-for-two-node-cpu-training-6019b43ec793-20260527T153041013059+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d13ad575a741

## What looked useful

Full-exchange two-node gossip uses the same averaging matrix and dense gradient payload as two-node all-reduce; the measured parameter and loss trajectories matched exactly within the 1e-12 threshold. An under-mixed gossip control diverged worker parameters and did not improve final loss.

## Boundaries and scale limits

Evidence is from a single-process NumPy simulation with synthetic non-IID logistic regression, not a real two-machine network benchmark or large neural model training run. It tests optimizer equivalence directly but not distributed-system runtime overheads.

## Claim scope

For two simulated CPU workers using dense full-gradient exchange every step, symmetric gossip-averaged gradients are algebraically and empirically identical to ordinary two-worker all-reduce averaged gradients on the tested logistic-regression task.

## Why it stopped

Proxy/local early falsification of the exact two-node full-exchange averaged-gradient claim: the tested gossip average is the same optimizer operation as all-reduce, so it has no distinct mechanism to validate at larger scale without changing the protocol.

## Recommended next action

Stop this exact idea as no-paper: any next useful test must change the protocol to compressed, stale, asynchronous, or periodic/local gossip and compare against all-reduce at matched communication budget.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaged-gradients-for-two-node-cpu-training-6019b43ec793`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
