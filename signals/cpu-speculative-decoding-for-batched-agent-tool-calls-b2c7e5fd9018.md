# CPU Speculative Decoding for Batched Agent Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-for-batched-agent-tool-calls-b2c7e5fd9018`
Run ID: `cpu-speculative-decoding-for-batched-agent-tool-calls-b2c7e5fd9018-20260612T234931952674+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce43259ae602

## What looked useful

High-regularity block-2 speculation reduced target calls by 43.5% with 83.4% mean acceptance, but five-seed dim-256 repeats averaged 0.920x wall speedup. Low-regularity block-4 repeats averaged 0.766x wall speedup with 27.8% call reduction and 1.355x target-token overhead. The mechanism reduces calls, but robust CPU speedup needs very high draft accuracy and small blocks.

## Boundaries and scale limits

Synthetic tokenizer and tool-call generator; NumPy dense-matmul CPU target proxy; trie draft rather than learned draft model; no real LLM, KV-cache, grammar decoder, or production scheduler. All runs were short local CPU probes below the 15-minute CPU-only limit.

## Claim scope

In a synthetic CPU verifier benchmark for batched JSON-like agent tool calls, trie-drafted speculative decoding reliably reduced target invocations for schema-heavy outputs but did not produce stable wall-clock speedup once extra verified-token work was included.

## Why it stopped

Proxy/local evidence is mixed: target-call reduction is supported, but stable wall-clock improvement is not supported in the synthetic CPU benchmark.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is a bounded real CPU inference follow-up using a small target/draft model pair on structured tool-call prompts, requiring stable latency speedup above 1.15x at equal output correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Inference Check for Speculative Tool-Call Decoding
- Success threshold: Mean wall-clock latency speedup >= 1.15x with median >= 1.10x, exact output correctness unchanged, and no low-regularity control showing a misleading positive.
- Stop condition: Stop if block-2 high-regularity real-inference runs average below 1.05x speedup or if output correctness differs from baseline.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-for-batched-agent-tool-calls-b2c7e5fd9018`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
