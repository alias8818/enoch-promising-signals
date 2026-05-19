# Paraphrased LLM-Agent Memory Grounding Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `paraphrased-llm-agent-memory-grounding-benchmark-8e4fcaa0b9`
Run ID: `paraphrased-llm-agent-memory-grounding-benchmark-8e4fcaa0b9-20260519T122107243904+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fce03dab0611

## What looked useful

Lexical BM25 achieved 100.0% top-1 on canonical queries but only 32.3% on paraphrased queries; a synonym-normalized diagnostic BM25 reached 100.0% on paraphrases, exceeding the predeclared 20 percentage point recovery threshold.

## Boundaries and scale limits

Synthetic templates only; no human paraphrases, no deployed LLM agent, no persistent memory writes, no answer generation faithfulness check, and the paraphrase-aware recovery baseline is a hand-authored synonym normalizer rather than an off-the-shelf semantic retriever.

## Claim scope

Tier 1 controlled synthetic retrieval-grounding benchmark with 96 memories and 192 paired canonical/paraphrased queries shows that paraphrased queries can expose memory-grounding failures hidden by canonical queries.

## Why it stopped

The Tier 1 direct test produced a useful mechanism signal but remains synthetic and uses an oracle-like hand-authored normalization baseline, so it is no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up using human or LLM-generated paraphrases plus an off-the-shelf embedding retriever and answer-generation grounding check; do not write a paper from this synthetic Tier 1 result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human/LLM Paraphrase Memory Grounding With Semantic Retrieval Baselines
- Success threshold: Lexical paraphrase top-1 is at least 20 percentage points below canonical top-1, and a non-oracle semantic method improves paraphrase top-1 by at least 15 percentage points over lexical BM25 while reducing canonical top-1 by no more than 5 points.
- Stop condition: Stop if lexical BM25 does not degrade by at least 20 points on the paraphrase set or if no non-oracle semantic method improves paraphrase top-1 by at least 10 points over lexical BM25.

## Evidence references

- Artifact root: `<local-path>/projects/paraphrased-llm-agent-memory-grounding-benchmark-8e4fcaa0b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
