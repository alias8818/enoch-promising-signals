# Network-Emulated Delta-Compressed Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `network-emulated-delta-compressed-distributed-training-76302dce52`
Run ID: `network-emulated-delta-compressed-distributed-training-76302dce52-20260522T111401428149+0000`

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

- Parent run decision: Home Delta-Compressed Distributed: enoch://control-plane/projects/home-delta-compressed-distributed-2615551bb97b/runs/home-delta-compressed-distributed-2615551bb97b-20260522T110504893596+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e0acb91f60c2

## What looked useful

Top-k 1%, top-k 5%, and sign error-feedback compression all matched dense final quality within the Tier 1 threshold; byte reductions were large, but estimated network speedups were only about 2.13x to 2.37x because latency dominated the tiny-model synchronization path.

## Boundaries and scale limits

Toy synthetic classification, two local workers, single process, analytic network timing, no real sockets, no tc/netem, no NCCL/TCP, no large model, no long-horizon convergence or robustness study.

## Claim scope

In a deterministic two-worker local synchronous SGD test on a small MLP, residual delta-compressed gradient synchronization preserved final accuracy/loss while reducing transmitted synchronization bytes by 9.96x to 49.8x versus dense synchronization under a 10 Mbps, 10 ms analytically emulated network.

## Why it stopped

Tier 1 small direct mechanism evidence is positive but remains a no-paper result because network behavior was analytically emulated and the task/model were too small for publication-grade distributed-training claims.

## Recommended next action

Run a bounded four-worker torch.distributed or multiprocessing test with actual tc/netem-shaped loopback links and measured wall-clock step time, stopping if compressed sync fails to preserve at least 98% of dense accuracy or 1.05x dense loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Netem-shaped multi-process delta-compressed synchronization
- Success threshold: Compressed sync must achieve >=98% of dense accuracy, <=1.05x dense loss, >=5x byte reduction, and >=1.5x measured step-time speedup under shaped bandwidth-constrained networking.
- Stop condition: Stop as unsupported if all compressed variants either miss the quality threshold or fail to improve measured step time by 1.5x despite reducing bytes.

## Evidence references

- Artifact root: `<local-path>/projects/network-emulated-delta-compressed-distributed-training-76302dce52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
