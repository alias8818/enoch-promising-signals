# Suffix-Tree Speculative Decoding from Target KV-Cache History

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-from-target-kv-cache-history-a8b51ed1b0b8`
Run ID: `suffix-tree-speculative-decoding-from-target-kv-cache-history-a8b51ed1b0b8-20260527T224252049243+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/565444d16177

## What looked useful

Synthetic repetitive traces reached 2.864 mean accepted tokens per attempt and a 3.860x estimated target-pass upper bound; shuffled project-prompt control reached only 1.011x and low-repetition synthetic reached 1.000x.

## Boundaries and scale limits

No transformer model, no real KV-cache implementation, no end-to-end latency measurement, no assistant-model speculative decoding comparison, and only synthetic plus small local prompt traces were tested.

## Claim scope

Trace-level online exact-suffix history can draft useful multi-token continuations on highly repetitive ordered token streams, but it collapses on shuffled or mostly-novel controls.

## Why it stopped

Bounded trace-level proxy supports a workload-specialized mechanism but is insufficient for a serving or paper claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the concrete next test is an in-decoder benchmark on model-generated repetitive and non-repetitive traces with measured KV/search overhead and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: In-decoder suffix-history speculative decoding benchmark
- Success threshold: At least 1.25x end-to-end latency improvement on repetitive model-generated workloads with no regression above 5% on non-repetitive controls.
- Stop condition: Stop if accepted-token gains disappear on model-generated traces or if suffix-index/KV overhead removes the target-pass savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-from-target-kv-cache-history-a8b51ed1b0b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
