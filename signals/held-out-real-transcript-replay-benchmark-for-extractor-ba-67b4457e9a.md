# Held-out real transcript replay benchmark for extractor-backed compressed state memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-real-transcript-replay-benchmark-for-extractor-ba-67b4457e9a`
Run ID: `held-out-real-transcript-replay-benchmark-for-extractor-ba-67b4457e9a-20260614T095312131064+0000`

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

- Parent run decision: Compressed State Memory for Repeated Agent Tasks: enoch://control-plane/projects/compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c/runs/compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c-20260614T025451767109+0000
- Parent run decision: Extractor-backed compressed state memory on real repeated-agent transcripts: enoch://control-plane/projects/extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30/runs/extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30-20260614T044802065894+0000

## What looked useful

Extractor compressed state reached 1.000 accuracy using 30.5% of full transcript characters, versus 0.392 recency-window and 0.958 flat-retrieval baselines. Low-budget and value-only ablations dropped to 0.225 and 0.000 accuracy, supporting the typed binding mechanism.

## Boundaries and scale limits

Small single-project corpus; deterministic extractor; templated fact questions; no LLM extraction, noisy paraphrases, human grading, multi-session persistence, or external/private transcript corpus.

## Claim scope

On a deterministic, sanitized project-local Enoch transcript/control-plane replay benchmark with 120 fixed-seed held-out fact queries, typed extractor-backed compressed state matched full-transcript accuracy and exceeded recency and flat-retrieval baselines modestly.

## Why it stopped

No-paper useful signal: Tier 2 local evidence supports the mechanism, but corpus size and deterministic templating are insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on multiple independent real transcripts with a live LLM extractor, paraphrased held-out queries, and human-reviewed answer grading before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-transcript LLM extractor replay benchmark with paraphrased held-out queries
- Success threshold: Extractor compressed memory accuracy >= 0.90, at least +0.10 over recency window, no worse than -0.03 versus flat retrieval, <= 0.40 full-transcript context size, and typed/value ablations show >= 0.20 accuracy gap.
- Stop condition: Stop as negative if extractor accuracy falls below 0.80, if flat retrieval exceeds extractor by more than 0.10 at comparable budget, or if human grading shows unsupported answer rate above 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-real-transcript-replay-benchmark-for-extractor-ba-67b4457e9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
