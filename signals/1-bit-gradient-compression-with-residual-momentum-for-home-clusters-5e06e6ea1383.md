# 1-bit gradient compression with residual momentum for home clusters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-gradient-compression-with-residual-momentum-for-home-clusters-5e06e6ea1383`
Run ID: `1-bit-gradient-compression-with-residual-momentum-for-home-clusters-5e06e6ea1383-20260529T183153395862+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e63c8b435f0c

## What looked useful

The mechanism is locally viable as a communication-volume reduction proxy: compressed methods matched or slightly exceeded dense validation accuracy in 600-step and 3000-step runs while sending about 32x fewer modeled gradient bytes. The residual-momentum variant improved over plain error feedback in the lower-LR persistence run but was weaker than plain sign compression, so the residual-momentum novelty claim is not paper-ready.

## Boundaries and scale limits

No real multi-node network, no NCCL/socket transport, no production bit packing overhead, no GPT-2-small-class or larger task, and no robustness sweep over worker count, bandwidth, latency, or non-IID data severity.

## Claim scope

Single-host PyTorch simulation of 4-worker synchronous data-parallel MLP training on a synthetic teacher-generated classification task. 1-bit sign compression variants reduced modeled gradient bytes by 31.94x and preserved dense-level validation accuracy; residual-momentum sign was trainable and dense-competitive but did not beat the simpler sign-only baseline.

## Why it stopped

Bounded proxy evidence supports 1-bit compression viability but does not support a publication-grade residual-momentum improvement over a simpler sign baseline.

## Recommended next action

Stop this run as no-paper useful signal; next run should test actual bit-packed communication with network-emulated bandwidth/latency and compare wall-clock throughput plus convergence against dense all-reduce and plain sign.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Network-emulated bit-packed 1-bit training for home-cluster links
- Success threshold: At least 1.5x wall-clock training-step speedup over dense exchange under a constrained-link setting, with final validation accuracy no more than 1 percentage point below dense and residual-momentum sign outperforming plain sign or clearly explaining why plain sign is preferable.
- Stop condition: Stop if bit packing plus communication overhead erases the modeled bandwidth advantage or if compressed validation accuracy drops more than 1 percentage point below dense in two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-gradient-compression-with-residual-momentum-for-home-clusters-5e06e6ea1383`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
