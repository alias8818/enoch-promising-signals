# KV-cache prompt-lookup decoding benchmark on real copy-heavy workloads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-prompt-lookup-decoding-benchmark-on-real-copy-hea-310a495b95`
Run ID: `kv-cache-prompt-lookup-decoding-benchmark-on-real-copy-hea-310a495b95-20260629T164513721052+0000`

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

- Parent run decision: Prompt-Lookup Spec Decoding on GB10 (Zero Draft VRAM): enoch://control-plane/projects/prompt-lookup-spec-decoding-on-gb10-zero-draft-vram-26da0fd351dc/runs/prompt-lookup-spec-decoding-on-gb10-zero-draft-vram-26da0fd351dc-20260629T163001921692+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8432b9a0e5b0

## What looked useful

Prompt lookup is worth further benchmarking for copy-heavy decoding because throughput gains were large on two model sizes, but output divergence from greedy baseline was frequent (12/16 on 0.5B, 7/8 on 3B) and full exact-copy rates were low (12.5% and 25.0%).

## Boundaries and scale limits

Single GB10 worker; 2 smoke, 16 medium 0.5B, and 8 confirmation 3B examples; local installed files as corpus; no production traces, no larger 7B+ confirmation, no parameter sweep, and no token-level equivalence instrumentation beyond generated text comparison.

## Claim scope

On a bounded GB10 GPU benchmark using real local source/document spans and Qwen2.5 0.5B/3B instruct models, Transformers prompt-lookup decoding produced 3.22x to 7.58x mean tokens/s speedups versus greedy baseline on controlled exact-copy prompts, but it did not establish baseline-output equivalence or high task fidelity.

## Why it stopped

Local proxy evidence supports a speed mechanism but not a reliable drop-in or paper-ready claim because prompt-lookup outputs often diverged from baseline and copy-task fidelity was low.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with token-id equivalence, task-quality metrics, copied-token fraction, and a parameter sweep before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level equivalence and quality sweep for prompt-lookup decoding on copy-heavy tasks
- Success threshold: Across at least 100 real copy-heavy examples, prompt lookup achieves at least 2x mean tokens/s with either at least 99% token-level equivalence to greedy baseline or no statistically meaningful task-quality degradation.
- Stop condition: Stop early if any tested setting has more than 1% unexplained token-level divergence without compensating task-quality gains, or if mean speedup stays below 1.5x on copied-token-fraction examples above 50%.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-prompt-lookup-decoding-benchmark-on-real-copy-hea-310a495b95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
