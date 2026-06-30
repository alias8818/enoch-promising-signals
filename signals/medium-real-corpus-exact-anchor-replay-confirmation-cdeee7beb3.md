# Medium real-corpus exact-anchor replay confirmation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `medium-real-corpus-exact-anchor-replay-confirmation-cdeee7beb3`
Run ID: `medium-real-corpus-exact-anchor-replay-confirmation-cdeee7beb3-20260526T223811317796+0000`

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

- Parent run decision: Chunked Pretraining with Exact-Anchor Replay: enoch://control-plane/projects/chunked-pretraining-with-exact-anchor-replay-98632728b87f/runs/chunked-pretraining-with-exact-anchor-replay-98632728b87f-20260525T034821640858+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

Exact anchors were real and reversible: frequency anchors covered about 11.0% of held-out bytes and reduced uncompressed replay bytes to 0.9957x raw on average. However, the entropy-coded replay stream was consistently worse than compressing the original bytes directly, so standalone anchor replay preprocessing is not a viable compression path under the stated threshold.

## Boundaries and scale limits

Validated on 44 real-text files, 273 chunks of 65,536 bytes, five fixed seeds, 48 train chunks and 16 held-out chunks per seed, 4,096 anchors, and gzip/zlib/bz2/lzma backends. It did not test zstd, web-scale corpora, compressor-native dictionary integration, neural compression, or downstream model/tokenizer effects.

## Claim scope

On the cached real-text corpus and five fixed train/test splits, exact-anchor replay preprocessing with dictionary-inclusive byte-exact serialization does not improve standard entropy compression. The best anchor variant increased gzip size by 14.78%, bz2 size by 15.40%, and lzma size by 16.08% on average, with 0 of 5 wins for each backend.

## Why it stopped

Direct medium real-corpus validation failed the follow-up success threshold: anchor-preprocessed gzip/zlib/bz2/lzma had 0/5 seed wins and increased compressed size by roughly 15% for the best anchor variant.

## Recommended next action

Stop this standalone exact-anchor replay preprocessing line; only revisit anchors through compressor-native dictionary integration or a different downstream objective, not as a separate entropy-coded replay transform.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-corpus-exact-anchor-replay-confirmation-cdeee7beb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
