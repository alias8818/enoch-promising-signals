# Live LLM repeated prompt-anchor context consumption test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-repeated-prompt-anchor-context-consumption-test-be652b9c0c`
Run ID: `live-llm-repeated-prompt-anchor-context-consumption-test-be652b9c0c-20260621T212632441771+0000`

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

- Parent run decision: Prompt-Anchored Self-Speculation via Repetition and Idiom Detection: enoch://control-plane/projects/prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc/runs/prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc-20260621T192101578755+0000
- Parent run decision: Live LLM PASS transcript validation for repeated prompt-anchor features: enoch://control-plane/projects/live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442/runs/live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442-20260621T200901721971+0000

## What looked useful

Across 12 fixed seeds and four strategies, repeated full-anchor injection reached 156,592 mean final context tokens at 64 turns, with 91.3% of the context attributable to anchors. It overflowed 8k, 32k, and 128k windows at turns 4, 14, and 53 respectively, while the no-anchor baseline did not overflow 32k or 128k within 64 turns.

## Boundaries and scale limits

Evidence is exact token accounting with tiktoken:gpt-4o over deterministic replay transcripts. It does not measure live remote LLM billing, hidden provider-side overhead, latency, answer quality, or attention degradation.

## Claim scope

For the actual Enoch controller prompt used in this project, repeatedly reinserting the full prompt anchor into a growing chat transcript causes tokenizer-visible context consumption to grow about 11.6x faster than a no-anchor baseline and to dominate the prompt by 64 turns.

## Why it stopped

The mechanism is supported for direct context-token consumption, but the run is not a live remote LLM quality or billing validation and therefore is not paper-positive.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should call one or two live LLM APIs with the same transcript schedules and measure billed input tokens, latency, and task accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM billing and quality validation for repeated prompt anchors
- Success threshold: Repeated full-anchor condition shows at least 5x higher billed/provider-reported input tokens than no-anchor and at least 4x higher than compact-anchor at 64 turns, without a compensating accuracy gain over compact-anchor.
- Stop condition: Stop if provider-reported input tokens differ by less than 2x from compact-anchor at 64 turns or if API access/model terms prevent measuring billed tokens or equivalent prompt-token usage.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-repeated-prompt-anchor-context-consumption-test-be652b9c0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
