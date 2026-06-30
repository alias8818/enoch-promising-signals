# LLM-integrated exact-anchor memory on semi-real home transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-integrated-exact-anchor-memory-on-semi-real-home-trans-076b7e483f`
Run ID: `llm-integrated-exact-anchor-memory-on-semi-real-home-trans-076b7e483f-20260607T155008545135+0000`

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

- Parent run decision: Long-Context Memory with Exact Anchors and Compressed State for Home AI: enoch://control-plane/projects/long-context-memory-with-exact-anchors-and-compressed-state-for-home-ai-a495c261e634/runs/long-context-memory-with-exact-anchors-and-compressed-state-for-home-ai-a495c261e634-20260607T102309018504+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

Across the primary 160-transcript run, exact-anchor memory achieved 1.000 anchor accuracy and 0.000 wrong-citation rate on 1,576 anchored questions, versus BM25 chunk retrieval at 0.468 accuracy and 0.532 wrong-citation rate. Three additional bounded runs, including a higher-noise setting, also met the predefined threshold.

## Boundaries and scale limits

The evidence is limited to generated semi-real transcripts, two fact schemas, deterministic parsing, and an LLM-facing answer payload; it does not test real household transcripts, human-authored questions, or end-to-end LLM generation.

## Claim scope

In a controlled generated home-transcript task with line-level gold anchors for item-location and device-state questions, a parsed exact-anchor memory layer retrieved and cited the correct transcript line more reliably than lexical chunk retrieval and recency baselines.

## Why it stopped

Tier 1 direct mechanism threshold was met, but this remains no-paper evidence because the data and parser are controlled/generated and no real LLM answer generation was evaluated.

## Recommended next action

Run a bounded end-to-end follow-up with held-out human-written or independently generated transcripts and a small LLM prompted with either exact-anchor memory payloads or chunk-retrieval payloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end LLM exact-anchor memory on held-out home transcripts
- Success threshold: On at least 300 anchored questions, exact-anchor prompting achieves answer accuracy within 5 percentage points of chunk prompting and reduces wrong/unsupported citation rate by at least 25 absolute percentage points.
- Stop condition: Stop if exact-anchor prompting fails to reduce wrong/unsupported citations by at least 10 absolute percentage points or if parser misses exceed 20 percent of answerable questions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-integrated-exact-anchor-memory-on-semi-real-home-trans-076b7e483f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
