# Standard-server queue-depth knee validation with repeated arrival traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `standard-server-queue-depth-knee-validation-with-repeated-c6d2bea14d`
Run ID: `standard-server-queue-depth-knee-validation-with-repeated-c6d2bea14d-20260608T062645323670+0000`

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

- Parent run decision: Queue Depth Scheduling for Bounded GPU Worker Throughput: enoch://control-plane/projects/queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232/runs/queue-depth-scheduling-for-bounded-gpu-worker-throughput-7c39fed74232-20260607T214611877457+0000
- Parent run decision: Queue-depth knee validation on real single-GPU model serving traces: enoch://control-plane/projects/queue-depth-knee-validation-on-real-single-gpu-model-servi-51e9c892f2/runs/queue-depth-knee-validation-on-real-single-gpu-model-servi-51e9c892f2-20260608T020253276813+0000

## What looked useful

Repeated finite arrival traces produced high-load queue-depth and latency knees, but the same knees appeared in Poisson, shuffled-repeat, and empirical-renewal controls. Bursty traces were worse than Poisson, but exact repetition was not consistently worse than distribution-preserving controls, so the repeated-trace-specific mechanism is unsupported.

## Boundaries and scale limits

No production traces, multi-server effects, load-balancer dynamics, admission control, or real service-time measurements were tested. The result is not a datacenter serving validation and is not paper-positive.

## Claim scope

Bounded CPU simulation of a standard FCFS single-server queue with exponential service, fixed seeds, repeated synthetic arrival traces, shuffled-repeat controls, empirical-renewal controls, and a Poisson/M/M/1-style baseline.

## Why it stopped

Medium fixed-seed direct simulation with ablations and a real Poisson baseline falsified the repeated-trace-specific knee mechanism within the tested standard-server scope.

## Recommended next action

Stop this follow-up as a useful negative result; only revisit if externally validated traces show exact repetition beating shuffled and empirical-renewal controls on predeclared queue-depth and tail-latency knee thresholds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/standard-server-queue-depth-knee-validation-with-repeated-c6d2bea14d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
