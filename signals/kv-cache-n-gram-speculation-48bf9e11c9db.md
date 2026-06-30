# KV-Cache N-Gram Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculation-48bf9e11c9db`
Run ID: `kv-cache-n-gram-speculation-48bf9e11c9db-20260603T160220849145+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2995134c597b

## What looked useful

Best proxy call reduction was 18.589% at draft length 16, but token-level proposal acceptance was only 1.658% with 11.035 wasted proposed tokens per evaluated token. A lower-waste draft length 2 setting saved 13.843% proxy calls but still wasted 1.361 proposed tokens per evaluated token and had median accepted run 0.

## Boundaries and scale limits

No live transformer verifier, no KV-cache memory benchmark, no generated-output trace, no latency measurement, and no comparison to a learned draft model. Results should not be treated as full serving validation.

## Claim scope

Bounded trace-level proxy on 100,000 GPT-2-tokenized WikiText-2 tokens shows naive history n-gram proposals have measurable acceptance above random prior-token copying but poor proposal efficiency.

## Why it stopped

Proxy evidence is useful but not paper-positive: n-gram reuse has signal, yet acceptance is too sparse and proposal waste too high for a compelling standalone serving claim without a substantially different gated design.

## Recommended next action

Stop naive always-propose n-gram speculation as a paper path; if continuing, test a high-precision gated n-gram variant in a real KV-cache serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: High-Precision Gated N-Gram KV-Cache Speculation
- Success threshold: At least 10% end-to-end latency improvement over standard KV-cache decoding with no output change under deterministic decoding, and less than 0.5 wasted verified draft tokens per generated token.
- Stop condition: Stop if gated proposals save less than 5% latency or require more than 0.5 wasted verified draft tokens per generated token on both tested text regimes.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculation-48bf9e11c9db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
