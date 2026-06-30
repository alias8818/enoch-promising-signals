# Gossip Averaging Home Distributed

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-home-distributed-1398cf08cc9b`
Run ID: `gossip-averaging-home-distributed-1398cf08cc9b-20260523T051234493702+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Ideal connected fp32 gossip reached median RMSE 6.68e-06 in 600 rounds over 20 seeds, validating the primitive. The 128-node degree-4 home sparse/churn fp32 case had 0% success and median final RMSE 0.0736 after 600 rounds; a 5000-round extension still missed <=1e-3 with median RMSE 0.00121 and 0.786 MB/node. Int8 reduced payload but added drift and also missed target; int4 produced large drift.

## Boundaries and scale limits

Synthetic only; 64-dimensional vectors, 64-128 nodes, static overlays, randomized online churn/loss, no real NAT traversal, no residential latency traces, no model-training downstream task, and no deployed multi-host run.

## Claim scope

Bounded synthetic average-consensus test: naive randomized pairwise gossip is mechanically valid on an ideal connected fp32 overlay, but it does not reach <=1e-3 RMSE within practical round/payload budgets under the tested 128-node sparse home overlay with churn and loss.

## Why it stopped

Proxy/local simulation early-falsified the naive home-distributed gossip averaging hypothesis under the tested sparse/churny budget; this is not a full real-world deployment validation.

## Recommended next action

Stop this naive-gossip line as no-paper evidence; next bounded test should evaluate accelerated or mass-preserving gossip overlays against the same <=1e-3, <=1200-round, <=0.25 MB/node threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Accelerated Home Gossip Averaging With Mass-Preserving Compression
- Success threshold: Median final RMSE <=1e-3, success rate >=0.8, median rounds to 1e-3 <=1200, median payload <=0.25 MB/node, and median mean drift norm <=1e-3.
- Stop condition: Stop if no tested accelerated/compressed variant reaches <=1e-2 within 1200 rounds or if quantization drift remains above 1e-3 after error-feedback/mass-preserving correction.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-home-distributed-1398cf08cc9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
