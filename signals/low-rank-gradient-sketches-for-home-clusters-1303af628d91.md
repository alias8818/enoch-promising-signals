# Low-Rank Gradient Sketches for Home Clusters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `low-rank-gradient-sketches-for-home-clusters-1303af628d91`
Run ID: `low-rank-gradient-sketches-for-home-clusters-1303af628d91-20260607T090410237136+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14562d0f635d

## What looked useful

Across three seeds, rank4+error-feedback matched dense accuracy within -0.0003 mean absolute accuracy while cutting upload bytes from 579.5 MB to 21.6 MB per 180 steps and modeled communication from 186.9 s to 8.34 s. Rank1+error-feedback retained within -0.0090 mean accuracy while cutting upload bytes to 7.1 MB. Rank1 without error feedback lost about 0.40 accuracy, showing error feedback is essential.

## Boundaries and scale limits

Not a real multi-node home cluster; one synthetic task; 201k-parameter MLP; exact SVD rather than randomized production sketching; 180 training steps; communication is modeled from bytes, bandwidth, and latency rather than measured over a network.

## Claim scope

On a single-GB10 simulated 4-worker data-parallel teacher-classification task, exact low-rank gradient sketches with error feedback reduced modeled 25 Mbps gradient communication by 22x to 50x while preserving dense-like final accuracy over 180 steps; sketches without error feedback caused large convergence loss.

## Why it stopped

No-paper closure: this is useful local simulated evidence, but real-network and standard-task validation are required before a paper claim.

## Recommended next action

Run a bounded direct follow-up on 2-4 real home-cluster nodes using measured network wall-clock, a randomized PowerSGD-style compressor, and one standard dataset/model baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-node validation of error-feedback low-rank gradient sketches for home clusters
- Success threshold: At least 5x measured communication-time reduction versus dense with final accuracy within 1 percentage point on the standard task and no worse than 2 percentage points on the synthetic task.
- Stop condition: Stop if measured wall-clock speedup is below 2x, if accuracy loss exceeds 3 percentage points for all sketch ranks, or if compressor overhead exceeds communication savings.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-gradient-sketches-for-home-clusters-1303af628d91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
