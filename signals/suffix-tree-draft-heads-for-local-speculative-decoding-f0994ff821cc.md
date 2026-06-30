# Suffix-Tree Draft Heads for Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-draft-heads-for-local-speculative-decoding-f0994ff821cc`
Run ID: `suffix-tree-draft-heads-for-local-speculative-decoding-f0994ff821cc-20260614T121512038472+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d3101b0c3e95

## What looked useful

Corrected medium benchmark: suffix_recent achieved first-token hit/accepted bytes per query of 0.971/7.383 on synthetic, 0.724/4.070 on project text, and 0.492/1.262 on Tiny Shakespeare, versus unigram_repeat 0.134/0.134, 0.163/0.380, and 0.147/0.147 respectively. This supports the mechanism but not a paper-ready serving claim.

## Boundaries and scale limits

Proxy only: byte tokens instead of model tokenizer IDs; corpus next bytes instead of an actual target model verifier distribution; no GPU target-forward latency, KV-cache, batching, or end-to-end speculative decoding throughput measurement; tiny/project/synthetic traces only.

## Claim scope

In causal byte-token trace-oracle benchmarks over one synthetic repeated trace, this project workspace text, and the first 120k bytes of Tiny Shakespeare, longest-suffix retrieval from already observed tokens produces substantially more oracle-accepted draft bytes than unigram-repeat and last-token-repeat controls.

## Why it stopped

Stopped after a corrected medium proxy benchmark because the mechanism signal is useful but not direct/full validation of local speculative decoding speedup.

## Recommended next action

Run a bounded tokenizer-level GPT-2-small decoding experiment that compares suffix retrieval against an n-gram/cache baseline on verifier acceptance and wall-clock tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-Level Suffix Drafting With GPT-2-Small Verification
- Success threshold: At least 1.20x wall-clock tokens/s over no-speculation and at least 10% more accepted draft tokens per verifier call than a matched n-gram/cache baseline on two non-synthetic prompt sets, without quality divergence under greedy decoding.
- Stop condition: Stop if suffix lookup overhead eliminates throughput gain, if accepted draft tokens are not higher than the n-gram/cache baseline, or if gains appear only on synthetic repetition.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-heads-for-local-speculative-decoding-f0994ff821cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
