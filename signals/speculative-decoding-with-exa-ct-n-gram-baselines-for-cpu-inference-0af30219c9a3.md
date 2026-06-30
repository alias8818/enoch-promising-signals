# Speculative Decoding with Exa ct N-gram Baselines for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-exa-ct-n-gram-baselines-for-cpu-inference-0af30219c9a3`
Run ID: `speculative-decoding-with-exa-ct-n-gram-baselines-for-cpu-inference-0af30219c9a3-20260607T195445183898+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

All speculative outputs exactly matched baseline greedy output. Copy-positive workload reached 1.76x in the primary run and 4.70x at draft_len=16; random workload was consistently slower with zero accepted tokens; mixed workload only benefited at short draft lengths and slowed at longer draft lengths.

## Boundaries and scale limits

Synthetic deterministic target stream with NumPy CPU verification cost; no real transformer, tokenizer, KV cache, batching, quantization, or production prompt distribution was tested.

## Claim scope

Bounded CPU proxy: exact prompt/history n-gram speculation preserves greedy output and can speed up high-overlap copy/edit-like continuations, but fixed longer drafts can slow mixed or low-reuse workloads despite reducing target calls.

## Why it stopped

Proxy evidence supports the mechanism conditionally but is not direct full LLM CPU inference validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a real CPU LLM follow-up comparing fixed versus adaptive n-gram draft length on code-edit and low-reuse prompt suites.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive N-Gram Draft Length for Real CPU LLM Prompt-Lookup Speculation
- Success threshold: Adaptive n-gram speculation must achieve at least 1.15x geometric-mean speedup over greedy baseline on mixed/code-edit CPU prompts while staying within 5% of baseline speed on low-reuse prompts and preserving exact greedy output.
- Stop condition: Stop if real CPU LLM runs show less than 1.05x speedup on code-edit prompts or more than 10% slowdown on low-reuse prompts after tuning draft length.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-exa-ct-n-gram-baselines-for-cpu-inference-0af30219c9a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
