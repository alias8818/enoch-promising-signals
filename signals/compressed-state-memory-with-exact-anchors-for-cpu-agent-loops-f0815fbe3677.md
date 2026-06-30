# Compressed-state memory with exact anchors for CPU agent loops

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-memory-with-exact-anchors-for-cpu-agent-loops-f0815fbe3677`
Run ID: `compressed-state-memory-with-exact-anchors-for-cpu-agent-loops-f0815fbe3677-20260613T085250737186+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bb53858795a

## What looked useful

Compressed summaries that preserve exact anchor slots matched full-transcript exact recall across five synthetic seeds while using about 0.025% of full-transcript query context. Lossy summaries and budgeted transcript search failed most exact-value queries.

## Boundaries and scale limits

No real operator traces, no LLM-in-the-loop compression, no adversarial retrieval, and no production agent-loop integration were tested. Evidence is local CPU-only synthetic replay over five seeds, 1250-1265 events per seed, and 480 exact-recall queries per seed.

## Claim scope

Deterministic synthetic CPU-agent replay tasks with arbitrary exact anchors for paths, flags, hashes, ports, and config values.

## Why it stopped

No-paper useful signal: the mechanism is supported in a bounded synthetic proxy, but direct real-trace evidence is required before a bounded paper claim.

## Recommended next action

Run the same exact-anchor interface on real repeated-agent traces with an LLM or production compressor, using exact recall, context tokens, and latency as primary metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace exact-anchor memory replay for CPU agent loops
- Success threshold: Exact-anchor memory reaches at least 0.98 exact recall, matches full transcript search within 1 percentage point, and uses at least 20x fewer mean query context tokens on the labeled trace corpus.
- Stop condition: Stop if exact-anchor memory falls below 0.95 exact recall or fails to reduce mean query context by 10x versus full transcript search.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-memory-with-exact-anchors-for-cpu-agent-loops-f0815fbe3677`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
