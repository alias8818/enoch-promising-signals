# CPU-Offloaded Draft Model Streaming

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-draft-model-streaming-6c5763ed08d5`
Run ID: `cpu-offloaded-draft-model-streaming-6c5763ed08d5-20260523T204203526646+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/71f733db03f9

## What looked useful

CPU-to-GPU token transfer is negligible, but CPU draft latency and runtime contention dominate. In calibrated actual-pipeline runs, block size 8 reached about 1204-1281 full-accept tok/s versus about 831-845 tok/s target-only, implying about 65-69% real acceptance is needed to break even; smaller blocks were fragile or negative.

## Boundaries and scale limits

No trained draft/target acceptance was measured, no production inference runtime was tested, and the target/draft models are small synthetic proxies rather than real deployed LLMs.

## Claim scope

On GB10 with synthetic random GPT-2-style models in PyTorch/Transformers, CPU-offloaded draft streaming can beat cached GPU target-only decoding only under high acceptance assumptions and favorable block sizes; actual Python-threaded overlap is much weaker than the ideal overlap model.

## Why it stopped

Synthetic/proxy systems run found mixed viability: ideal overlap looks promising, but actual threaded overlap needs high acceptance and is not robust enough for a paper claim.

## Recommended next action

Run a bounded trained-model deepen test with a real small draft/target pair and a lower-overhead overlap runtime; stop this run as no-paper useful systems evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Small-Model CPU Draft Acceptance and Overlap Test
- Success threshold: At least 1.2x accepted-token throughput over target-only cached decoding with measured acceptance >=70% at block size 8 across a reproducible held-out text sample.
- Stop condition: Stop if measured acceptance is below 60% at block size 8 or if actual overlapped throughput remains below target-only throughput after runtime overhead profiling.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-draft-model-streaming-6c5763ed08d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
