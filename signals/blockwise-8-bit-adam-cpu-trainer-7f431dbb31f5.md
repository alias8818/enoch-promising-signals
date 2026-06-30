# Blockwise 8-bit Adam CPU Trainer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adam-cpu-trainer-7f431dbb31f5`
Run ID: `blockwise-8-bit-adam-cpu-trainer-7f431dbb31f5-20260607T091948493962+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bde5126b6812

## What looked useful

The failure is localized to second-moment quantization: m8/v32 matched Adam32 at 100 steps, while m32/v8 and full m8/v8 collapsed. This suggests naive full blockwise 8-bit Adam is not viable, but stabilized second-moment quantization is a concrete follow-up target.

## Boundaries and scale limits

Tested only on one synthetic teacher/student MLP, CPU NumPy implementation, 100-160 optimizer steps, block sizes 256 and 1024 for full int8 and block size 1024 for mixed-state ablations. Not validated on real corpora, language models, PyTorch kernels, C++ fused CPU kernels, or long training runs.

## Claim scope

On a deterministic NumPy CPU synthetic MLP classification benchmark with about 2.14M float32 parameters, naive blockwise int8 quantization of both Adam first and second moments saves about 75% optimizer-state memory but fails convergence; quantizing only the first moment preserves short-run convergence while saving about 37% optimizer-state memory.

## Why it stopped

Direct bounded testing falsified the naive full blockwise int8 Adam CPU trainer as a convergence-preserving drop-in replacement; this is a proxy/local early falsification, not a full-scale language-model validation.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; the next concrete test is a second-moment-stabilized blockwise int8 Adam variant on the same benchmark plus one real small-model CPU benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized second-moment blockwise int8 Adam on CPU
- Success threshold: Stabilized m8/v8 finishes at least 160 steps within 1 percentage point test accuracy and 5% test loss of Adam32, keeps optimizer-state bytes at or below 40% of Adam32, and runs at no worse than 0.7x Adam32 throughput in a CPU implementation.
- Stop condition: Stop if stabilized m8/v8 still collapses or misses Adam32 by more than 5 percentage points accuracy on the synthetic benchmark, or if the throughput penalty is worse than 0.5x while using only local CPU execution.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-cpu-trainer-7f431dbb31f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
