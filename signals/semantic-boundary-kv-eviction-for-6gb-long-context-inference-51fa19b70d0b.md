# Semantic-boundary KV eviction for 6GB long-context inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b`
Run ID: `semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b-20260530T043315545164+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3de4fe3a8a0b

## What looked useful

Semantic-boundary retention achieved answerable rates of 0.877, 0.994, and 0.994 at 4,096, 8,192, and 16,384 retained tokens, versus sliding-window rates of 0.119, 0.234, and 0.455. It preserved old/recurrent synthetic facts but introduced hundreds of retained-token intervals, implying a real runtime fragmentation risk.

## Boundaries and scale limits

No real LLM serving, tokenizer, attention implementation, paged KV runtime, decode-throughput measurement, or human/natural benchmark was tested. Fact-anchor detection and segment salience were synthetic favorable assumptions.

## Claim scope

Synthetic 65,536-token segmented KV-retention probe with 512 retrieval-style queries and 4,096-16,384 retained-token budgets; semantic-boundary retention preserved synthetic fact anchors better than sliding-window retention under matched token budgets.

## Why it stopped

Proxy-only evidence supports the retention mechanism but is insufficient for a paper or full 6GB long-context inference validation.

## Recommended next action

Stop this run as a no-paper synthetic useful signal; next run should implement a small-transformer paged-KV benchmark with real prompts, matched KV memory, answer accuracy, and decode-throughput measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer paged-KV semantic-boundary eviction benchmark
- Success threshold: At least 20 percentage points higher answer accuracy than sliding-window eviction on old/recurrent queries at matched KV memory, with recent-query accuracy within 5 points and decode throughput no worse than 10%.
- Stop condition: Stop if semantic-boundary eviction fails to beat sliding-window accuracy by 10 percentage points on old/recurrent queries or causes more than 20% decode-throughput regression in the small-transformer benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
