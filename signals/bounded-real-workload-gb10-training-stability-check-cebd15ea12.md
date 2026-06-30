# Bounded Real-Workload GB10 Training Stability Check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-real-workload-gb10-training-stability-check-cebd15ea12`
Run ID: `bounded-real-workload-gb10-training-stability-check-cebd15ea12-20260612T233458646267+0000`

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

- Parent run decision: Canary-MiniTask Validation for Volunteer GB10 Training: enoch://control-plane/projects/canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013/runs/canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013-20260612T232441057400+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3474a9ab489f

## What looked useful

The Tier 1 direct test passed: smoke 20/20 and direct 600/600 CIFAR-10 training steps completed on GB10 CUDA with no non-finite events; direct-run loss fell from 2.21819 to 0.94422 mean over first/last 20 steps, throughput was 2419.25 samples/s after warmup, peak CUDA reserved memory was 2.693 GiB, process RSS stayed near 2.314 GiB, and sampled MemAvailable stayed above 110.669 GiB with swap disabled.

## Boundaries and scale limits

One seed, one small image dataset, one residual CNN, one bf16 precision mode, about 65 seconds of direct training. This does not validate GPT-2-small-class or larger language-model training, multi-hour stability, checkpoint/resume robustness, multi-seed behavior, or publication-grade comparisons.

## Claim scope

On this GB10 host, PyTorch 2.12 CUDA bf16 training completed a bounded real CIFAR-10 residual CNN workload for 600 optimizer steps with finite losses/gradients, 57.43% loss decrease, high sampled GPU utilization, and safe UMA memory posture.

## Why it stopped

Tier 1 controlled small direct test completed successfully and produced a useful no-paper stability signal; stopping because the current evidence is not publication-grade and the next meaningful step is a distinct bounded deepen follow-up.

## Recommended next action

Run a bounded deepen follow-up using a small transformer language-model training workload for 30-60 minutes on GB10 with checkpoint/resume validation, repeated seeds or repeated runs, and the same UMA/GPU telemetry thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 Transformer Training Stability With Checkpoint Resume
- Success threshold: Complete the planned transformer run and resume segment with no non-finite loss/gradient events, no sustained throughput collapse greater than 25% after warmup, MemAvailable remaining above 20 GiB, and final-window loss at least 10% below initial-window loss.
- Stop condition: Stop early if any non-finite loss/gradient occurs, MemAvailable drops below 20 GiB, the process is OOM-killed, checkpoint/resume fails, or throughput remains below 75% of warmup-adjusted baseline for three consecutive telemetry intervals.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-real-workload-gb10-training-stability-check-cebd15ea12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
