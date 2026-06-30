# Async gradient compression for home CPU training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `async-gradient-compression-for-home-cpu-training-c15204d24630`
Run ID: `async-gradient-compression-for-home-cpu-training-c15204d24630-20260608T092742122267+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1b9c9a573847

## What looked useful

Corrected 3-seed run: async dense val_acc 0.7515, 42.1 MB transfer, 9.30 s modeled time; async 1% top-k EF val_acc 0.7537, 0.84 MB transfer, 1.07 s modeled time. Sweep found 0.1%-0.25% top-k underfit while 1%-5% reached the dense-async accuracy band.

## Boundaries and scale limits

Single-process event simulation; synthetic classification data; small 17k-parameter MLP; SGD only; simulated network transfer; no real sockets, no multi-host scheduling, no language model, no AdamW, no long training run.

## Claim scope

On a small synthetic CPU-trained MLP with measured NumPy gradient and codec costs plus a 10 Mbps/5 ms event-simulated home-link model, asynchronous 1% top-k gradient compression with error feedback matched dense asynchronous SGD validation accuracy while reducing gradient transfer by about 50x and modeled wall time by about 8.7x.

## Why it stopped

No-paper useful signal: the mechanism is supported only by a small synthetic training task and simulated network transfer, not by direct real-network or language-model evidence.

## Recommended next action

Stop paper work for this run; run a bounded direct multiprocessing or two-host LAN validation using the same dense async and 1% top-k EF controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real multiprocessing validation of async 1% top-k error-feedback training on CPU
- Success threshold: 1% top-k EF achieves validation metric within 1% relative of dense async while reducing measured end-to-end wall time by at least 2x at 10 Mbps and showing bounded residual norms across seeds.
- Stop condition: Stop if real socket/process overhead eliminates the wall-time gain below 1.25x, or if validation quality is worse than dense async by more than 3% relative at 1%-5% top-k.

## Evidence references

- Artifact root: `<local-path>/projects/async-gradient-compression-for-home-cpu-training-c15204d24630`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
