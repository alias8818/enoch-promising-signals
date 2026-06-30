# KV-cache-aware suffix-trie speculation on a GPT-2-small-class target

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-aware-suffix-trie-speculation-on-a-gpt-2-small-cl-3495ca6eeb`
Run ID: `kv-cache-aware-suffix-trie-speculation-on-a-gpt-2-small-cl-3495ca6eeb-20260629T145843048926+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Suffix-Trie Tree Speculation Without Draft-Model VRAM: enoch://control-plane/projects/suffix-trie-tree-speculation-without-draft-model-vram-0c972fae9be2/runs/suffix-trie-tree-speculation-without-draft-model-vram-0c972fae9be2-20260629T142803699253+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f114b7da08bd

## What looked useful

Exact GPT-2-small-class runs showed zero token mismatches but 0.643x-0.903x mean speed versus cached greedy, low held-out acceptance (0.040-0.316), and increased target calls in every tested configuration. The best speed configuration remained slower at 0.903x.

## Boundaries and scale limits

Small prompt set, GPT-2-small-class only, greedy decoding only, batch size 1, no real production serving traces, no custom branchable KV-cache kernel, no 7B+ or datacenter-scale validation.

## Claim scope

On a local GB10 GPU with GPT-2 small, fp32 exact greedy decoding, target-generated suffix-trie traces, 12 held-out prompts, and five proposal configurations, KV-cache-aware suffix-trie speculation did not improve throughput over cached greedy decoding.

## Why it stopped

Direct local GPT-2-small-class evidence is a no-paper useful-signal negative: exact suffix-trie speculation was slower than cached greedy and increased target forwards under tested settings.

## Recommended next action

Stop this paper path; only revisit with real serving traces plus a cheap branchable KV-cache rollback implementation that can demonstrate target-call reduction before wall-clock benchmarking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Branchable KV-cache rollback for suffix-trie speculation on real repeated-prefix traces
- Success threshold: On held-out traces, zero token mismatches, at least 20% target-call reduction, and at least 1.10x mean tokens/s versus cached greedy on the same target and hardware.
- Stop condition: Stop if held-out acceptance remains below 50% for proposed tokens or if exact rollback overhead prevents positive target-call reduction on GPT-2-small-class after a bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-suffix-trie-speculation-on-a-gpt-2-small-cl-3495ca6eeb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
