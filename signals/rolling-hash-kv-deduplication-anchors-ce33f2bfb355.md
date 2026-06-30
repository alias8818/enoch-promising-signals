# Rolling-Hash KV Deduplication Anchors

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `rolling-hash-kv-deduplication-anchors-ce33f2bfb355`
Run ID: `rolling-hash-kv-deduplication-anchors-ce33f2bfb355-20260526T061231016294+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2df4cd4f2a67

## What looked useful

Rolling-hash chunk anchors produced 0% exact dedup on three Gutenberg texts and the shifted-boilerplate prompt case, and underperformed fixed 32-token chunks on the near-duplicate case (29.293% versus 65.691% duplicate tokens) while running several times slower in this implementation.

## Boundaries and scale limits

CPU-only Python probe; lowercase word/punctuation token ids; no production BPE tokenizer, transformer execution, GPU KV-cache layout, serving scheduler, or latency measurement. Natural corpus and generated prompts are not private production traces.

## Claim scope

Bounded local mechanism probe of exact token-span KV reuse using rolling-hash content-defined chunks over public-domain natural text and generated prompt-like repeated/near-duplicate streams.

## Why it stopped

Proxy early falsification: the tested rolling-hash chunk anchors did not recover useful exact KV-span reuse where expected and were inferior to a simpler fixed-chunk control on the main positive-control workload.

## Recommended next action

Stop this design as a no-paper useful negative; only revisit if a production-tokenized prompt trace shows frequent shifted exact repeats and a revised anchor rule beats fixed small chunks plus prefix-cache baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/rolling-hash-kv-deduplication-anchors-ce33f2bfb355`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
