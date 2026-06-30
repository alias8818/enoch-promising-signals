# Two-tier exact-anchor memory with semantic compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `two-tier-exact-anchor-memory-with-semantic-compression-b8977705879c`
Run ID: `two-tier-exact-anchor-memory-with-semantic-compression-b8977705879c-20260613T123032060477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd00523d3f50

## What looked useful

Semantic compression alone reached 0.000 exact accuracy and 0.408 semantic accuracy at 0.296 transcript memory ratio; two-tier exact-anchor plus semantic compression reached 1.000 exact accuracy and 0.408 semantic accuracy at 0.573 transcript memory ratio.

## Boundaries and scale limits

Synthetic generated transcripts, deterministic parser/scorer, no LLM summarizer or model-generated answers, no production vector store, no long-horizon persistence, and no real operator data.

## Claim scope

On a deterministic synthetic repeated-agent replay benchmark with 256 cases and 1024 tasks, a two-tier memory layout with compact exact anchor facts plus lossy semantic summaries preserved exact anchor recall while matching semantic-compression semantic accuracy.

## Why it stopped

Closed as no-paper useful signal: bounded synthetic evidence supports the mechanism but is not direct production or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with noisy human-authored or LLM-authored replay transcripts, persisted memory updates, and the same exact/semantic scoring matrix before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy replay validation for two-tier exact-anchor semantic memory
- Success threshold: Two-tier strategy achieves exact accuracy >= 0.90, semantic accuracy no worse than semantic-compression-only by more than 0.02 absolute, and memory ratio < 1.0 versus raw transcript.
- Stop condition: Stop if two-tier exact accuracy is below 0.80 or if memory ratio is >= 1.0 after compacting anchor facts on the noisy corpus.

## Evidence references

- Artifact root: `<local-path>/projects/two-tier-exact-anchor-memory-with-semantic-compression-b8977705879c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
