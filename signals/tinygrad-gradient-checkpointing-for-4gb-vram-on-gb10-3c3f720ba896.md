# TinyGrad gradient checkpointing for 4GB VRAM on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinygrad-gradient-checkpointing-for-4gb-vram-on-gb10-3c3f720ba896`
Run ID: `tinygrad-gradient-checkpointing-for-4gb-vram-on-gb10-3c3f720ba896-20260609T082943777101+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eca178203750

## What looked useful

tinygrad current source detects GB10 as sm_121, but local NVRTC rejects sm_121/sm_120/sm_100; sm_90 PTX is accepted and runs on GB10. DEV=NV fails with NV_ERR_NOT_SUPPORTED. Short forced-sm90 CUDA training completed with 0.221 s/step and 350 MB tinygrad end memory on the largest probe.

## Boundaries and scale limits

No explicit 4 GB allocator cap was enforced, no real checkpoint/rematerialization implementation was validated, and the largest direct run was a short 6-layer MLP-style stack rather than GPT-2-small-class training.

## Claim scope

On this GB10 host, current tinygrad lacks a public gradient-checkpointing API and default GB10 CUDA/NV backends fail smoke tests; forcing CUDA codegen to sm_90 runs short tinygrad training probes, but only normal training plus analytic checkpoint memory estimates were tested.

## Why it stopped

Proxy/early falsification of paper readiness: no direct checkpointing mechanism was available or validated, though GB10 backend compatibility and normal-training memory evidence were collected.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to implement or expose a tinygrad rematerialization primitive and rerun baseline-vs-checkpoint under an explicit 4 GB budget using the sm_90 GB10 workaround.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implement tinygrad rematerialization probe under a 4 GB budget on GB10
- Success threshold: Checkpointed run fits a configuration that baseline fails under the same 4 GB budget, gradients match baseline within a small numerical tolerance on the small test, and throughput remains at least 50% of baseline for the medium case.
- Stop condition: Stop if tinygrad autograd cannot support a correct rematerialization primitive without invasive framework changes, or if baseline and checkpointed memory use differ by less than 15% under direct telemetry.

## Evidence references

- Artifact root: `<local-path>/projects/tinygrad-gradient-checkpointing-for-4gb-vram-on-gb10-3c3f720ba896`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
