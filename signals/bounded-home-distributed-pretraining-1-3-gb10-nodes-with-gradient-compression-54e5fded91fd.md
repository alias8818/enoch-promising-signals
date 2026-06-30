# Bounded home distributed pretraining: 1-3 GB10 nodes with gradient compression

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `68`
Project ID: `bounded-home-distributed-pretraining-1-3-gb10-nodes-with-gradient-compression-54e5fded91fd`
Run ID: `bounded-home-distributed-pretraining-1-3-gb10-nodes-with-gradient-compression-54e5fded91fd-20260613T165059002917+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d25e02f83924

## What looked useful

Gradient compression can reduce modeled 3-node 1 Gbps exchange from about 181 ms/step for dense fp32 to about 5.7 ms for sign and 3.6 ms for top-k 1%, but aggressive compression worsened short-run loss. Dense fp16 preserved the dense loss trajectory while halving payload.

## Boundaries and scale limits

No real 2-3 physical-node GB10 run was performed; data were synthetic; model was small; communication was estimated from payload bytes and bandwidth rather than measured NCCL/Gloo traffic; run length was 80 steps.

## Claim scope

Single-GB10 CUDA toy pretraining probe plus byte-based 1-3 node communication estimates for a 4.24M-parameter transformer using dense fp32, dense fp16, sign, and top-k 1% error-feedback gradient transformations.

## Why it stopped

Useful proxy evidence was produced, but the core multi-node pretraining claim remains unvalidated because this worker has only one GB10 and used modeled communication rather than physical distributed traffic.

## Recommended next action

Stop this worker run; the next meaningful validation requires actual 2-3 GB10 nodes on a target home network with DDP/NCCL or equivalent and longer convergence checks.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/bounded-home-distributed-pretraining-1-3-gb10-nodes-with-gradient-compression-54e5fded91fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
