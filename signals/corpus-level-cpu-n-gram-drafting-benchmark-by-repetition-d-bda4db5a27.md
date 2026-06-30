# Corpus-Level CPU N-Gram Drafting Benchmark by Repetition Density

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `corpus-level-cpu-n-gram-drafting-benchmark-by-repetition-d-bda4db5a27`
Run ID: `corpus-level-cpu-n-gram-drafting-benchmark-by-repetition-d-bda4db5a27-20260605T202214806566+0000`

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

- Parent run decision: CPU-Only Speculative Decoding via N-Gram Drafting: enoch://control-plane/projects/cpu-only-speculative-decoding-via-n-gram-drafting-7498aec2fcf3/runs/cpu-only-speculative-decoding-via-n-gram-drafting-7498aec2fcf3-20260605T092024021998+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

Repetition density increased n-gram context hit rate and longer contexts recovered monotonic acceptance, but no tested condition met the pre-registered Tier 1 threshold; short contexts became ambiguous at high repetition and longer contexts delivered only 1.56x-1.62x high-vs-low lift rather than the required 2x.

## Boundaries and scale limits

Does not test real corpora, tokenizer effects, neural verifier acceptance, end-to-end speculative decoding latency, large corpus indexes, multi-threaded CPU serving, or GPU-assisted decoding.

## Claim scope

Controlled synthetic 250k-token CPU benchmark of corpus-level greedy n-gram drafting by repeated-span density, with n in {4, 8, 12, 16} and max draft length 16.

## Why it stopped

Pre-registered Tier 1 threshold failed in a direct controlled benchmark, though mechanism support was mixed rather than absent.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test adaptive context length or top-k continuation selection on real text/code corpora against no-draft and fixed-n greedy baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Corpus N-Gram Drafting on Real Corpora
- Success threshold: Adaptive/top-k drafting must improve accepted tokens per position by at least 25% over the best fixed-n greedy baseline in high-repetition buckets and must not regress low-repetition buckets by more than 5%, while maintaining at least 100k evaluated tokens/sec CPU throughput.
- Stop condition: Stop negative if adaptive/top-k drafting fails to beat the best fixed-n baseline by 25% in high-repetition buckets on either real corpus or if throughput falls below 100k evaluated tokens/sec.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-level-cpu-n-gram-drafting-benchmark-by-repetition-d-bda4db5a27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
