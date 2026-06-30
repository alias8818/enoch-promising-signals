# N-gram suffix tree speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-43e6cc142de8`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-43e6cc142de8-20260609T020903902249+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9e27228b3cd6

## What looked useful

Corpus suffix reuse can draft held-out continuations better than a constant baseline: the main run improved mean accepted bytes from 0.1498 to 0.8186 per 8-byte draft, but 57.3% of suffix proposals accepted zero bytes and full 8-byte acceptance was 0.32%. A trie-shaped suffix tree did not improve proposal quality over a flat n-gram table and used more memory.

## Boundaries and scale limits

No LLM target model, no logits-based acceptance, no KV-cache or verification-batch measurement, no end-to-end decoding throughput. Largest run used 150k training bytes, 50k held-out bytes, 20k query positions, max context 12, draft length 8, and peak RSS about 849 MB inside Python.

## Claim scope

Byte-level held-out-text proxy on Tiny Shakespeare up to 200k bytes: longest-context n-gram suffix proposals improve exact accepted bytes over a constant baseline at microsecond lookup latency, but acceptance is sparse and memory grows quickly.

## Why it stopped

No-paper useful signal: bounded proxy evidence supports the suffix-reuse mechanism but not a practical or publication-grade speculative-decoding claim.

## Recommended next action

Stop this proxy-only run; if continuing locally, integrate a compact suffix drafter into a small CPU transformer decoding loop and require measured wall-clock tokens/sec improvement over greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM integration test for compact suffix drafter
- Success threshold: At least 10% end-to-end tokens/sec improvement over the no-drafter CPU decode baseline on a small transformer with no more than 256 MB additional drafter memory, and median accepted draft length above 1 token on real prompts.
- Stop condition: Stop as negative if end-to-end speedup is below 5%, median accepted draft length is zero, or drafter memory/maintenance overhead exceeds the saved verification time.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-cpu-43e6cc142de8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
