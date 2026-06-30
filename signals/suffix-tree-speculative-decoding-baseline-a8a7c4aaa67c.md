# Suffix-Tree Speculative Decoding Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-baseline-a8a7c4aaa67c`
Run ID: `suffix-tree-speculative-decoding-baseline-a8a7c4aaa67c-20260613T145958115678+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0a4cc9efb5b

## What looked useful

Naive longest-suffix drafting is very effective on highly repetitive template text, reaching 3.6478 accepted tokens/query and 85.98% full 4-token acceptance, but it is brittle on local natural text where fixed 4-gram outperformed it by 2.4191 versus 0.4490 accepted tokens/query.

## Boundaries and scale limits

No neural target model, no real speculative-decoding verification loop, no GPU serving latency, no KV-cache accounting, and only small local/proxy corpora. Results do not validate broad LLM serving speedups.

## Claim scope

A CPU-only offline probe of suffix-context draft proposals on one controlled repetitive synthetic corpus and one small local natural-text sample, measuring exact held-out token acceptance for draft_k=4.

## Why it stopped

Proxy evidence is mixed: it supports suffix-context drafting for repetitive text but early-falsifies the stronger claim that naive longest-suffix lookup is a robust general speculative-decoding baseline. This is not full validation.

## Recommended next action

Run a bounded deepen follow-up that adds calibrated suffix backoff/scoring and integrates the draft policy with a small transformer target to measure accepted tokens/sec against no-speculation and n-gram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated suffix backoff with small-transformer speculative decoding
- Success threshold: At least 10% accepted tokens/sec improvement over the best fixed n-gram control on the repetitive corpus without worse latency than no speculation or a material acceptance collapse on the natural-text prompt set.
- Stop condition: Stop if calibrated suffix variants fail to beat fixed n-gram accepted tokens/sec on repetitive text or add enough lookup overhead to lose end-to-end latency versus no speculation.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-baseline-a8a7c4aaa67c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
