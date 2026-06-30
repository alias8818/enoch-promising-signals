# Live-LLM quote-memory replay with target-hash scoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-llm-quote-memory-replay-with-target-hash-scoring-bc8adca3a5`
Run ID: `live-llm-quote-memory-replay-with-target-hash-scoring-bc8adca3a5-20260621T130502100445+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: LLM-in-the-loop hash-pinned quote memory under noisy repeated sessions: enoch://control-plane/projects/llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1/runs/llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1-20260621T120752308955+0000
- Parent run decision: Live-LLM hash-pinned quote memory under noisy repeated sessions: enoch://control-plane/projects/live-llm-hash-pinned-quote-memory-under-noisy-repeated-ses-3f72261bd7/runs/live-llm-hash-pinned-quote-memory-under-noisy-repeated-ses-3f72261bd7-20260621T124832195241+0000

## What looked useful

Target-hash scoring produced a direct exact-match metric, and structured/layered memory showed a paired advantage over flat retrieval (11 layered-only wins vs 2 flat-only wins, exact binomial p=0.02246). Layered memory did not outperform transcript search at this scale.

## Boundaries and scale limits

Single local 0.5B model, synthetic quotes, synthetic replay contexts, CPU-only run, no naturalistic repeated-agent sessions, no multi-model robustness, and no long-horizon persistence.

## Claim scope

On a 30-task synthetic quote replay suite with one local Qwen2.5-0.5B-Instruct-Q8_0 model, SHA-256 target-hash scoring cleanly measured exact quote replay; layered doctrine memory and transcript search each achieved 28/30 exact matches, flat retrieval achieved 19/30, and no/wrong-memory controls achieved 0/30.

## Why it stopped

Bounded live-model evidence supports the mechanism relative to flat retrieval and controls, but the run is synthetic and single-model, and layered memory ties transcript search rather than establishing a broader paper-ready result.

## Recommended next action

Stop as no-paper useful signal; next bounded deepen test should run the same target-hash harness across multiple model families and naturalistic replay traces before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model naturalistic target-hash quote replay validation
- Success threshold: Layered memory exact-hash match rate exceeds flat retrieval by at least 15 percentage points with paired p < 0.01 and is not worse than transcript search by more than 5 percentage points across model families.
- Stop condition: Stop if layered memory fails to beat flat retrieval by 10 percentage points on the first two model families or if failure audit shows extraction/scoring artifacts dominate observed differences.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-quote-memory-replay-with-target-hash-scoring-bc8adca3a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
