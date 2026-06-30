# Residual semantic compression on noisy real agent interaction traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-semantic-compression-on-noisy-real-agent-interact-15fb1d5c8d`
Run ID: `residual-semantic-compression-on-noisy-real-agent-interact-15fb1d5c8d-20260621T205135448920+0000`

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

- Parent run decision: Agent Memory: Residual Semantic Compression of Interaction Traces: enoch://control-plane/projects/agent-memory-residual-semantic-compression-of-interaction-traces-c65f09caa5b9/runs/agent-memory-residual-semantic-compression-of-interaction-traces-c65f09caa5b9-20260621T201532309208+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

Residual semantic compression reached 0.9000 accuracy at 0.2880 retained/raw token ratio with zero private-noise leakage and strongly beat flat first-seen summary accuracy, but it did not beat raw transcript search accuracy; transcript_search reached 0.9222 accuracy at the 80-token budget while leaking redacted noise in 0.7889 of cases.

## Boundaries and scale limits

No real private production traces, no LLM semantic extractor, no human-labeled unstructured trace set, and no long-horizon deployment behavior were tested. Results are bounded to symbolic controlled traces and deterministic retrieval/scoring.

## Claim scope

Tier-1 controlled generated repeated-agent traces with explicit project/key/value/revision facts, injected distractor events, stale values, redundant chatter, and redacted private-noise tokens under fixed token budgets.

## Why it stopped

Controlled Tier-1 evidence directly failed the required accuracy-gain threshold versus transcript_search, so this is mechanism support for compact privacy-preserving memory rather than a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should use sanitized real multi-session agent traces and a privacy-constrained transcript-search control with the same latest-state labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual compression on sanitized real agent traces with privacy-constrained transcript control
- Success threshold: Residual semantic compression accuracy >= 0.85, at least +0.10 absolute accuracy over privacy-constrained transcript search, retained/raw token ratio <= 0.35, private-noise leakage = 0, and stale-answer rate no worse than transcript_search by more than 0.02.
- Stop condition: Stop if residual compression fails to beat privacy-constrained transcript search by +0.10 absolute accuracy or leaks any redacted payload marker on the labeled trace set.

## Evidence references

- Artifact root: `<local-path>/projects/residual-semantic-compression-on-noisy-real-agent-interact-15fb1d5c8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
