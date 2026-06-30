# Evidence-ledger agent loop on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-on-cpu-1e2d770f944c`
Run ID: `evidence-ledger-agent-loop-on-cpu-1e2d770f944c-20260530T002811149670+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Corrected 10-seed run: ledger accuracy 0.99778 vs baseline 0.50797, absolute gain +0.48982; ledger trace-complete rate 1.0 vs baseline 0.66667; ledger mean latency 0.01175 ms/task vs baseline 0.00241 ms/task, about 4.98x relative but negligible absolute overhead; max RSS 24,800 KB.

## Boundaries and scale limits

Evidence is synthetic and local only: 10 seeds, 500 entities per seed, 15,000 documents and 6,000 tasks per seed. It does not validate natural-language claim decomposition, real retrieval corpora, stronger rerankers, LLM tool use, multi-turn agent behavior, or publication-grade robustness.

## Claim scope

On a deterministic synthetic CPU fact-checking benchmark with functional properties, stale/conflicting snippets, and no LLM dependency, an evidence-ledger loop improved answer accuracy and trace completeness over a newest-snippet retrieval baseline while keeping absolute latency and memory small.

## Why it stopped

Useful bounded synthetic signal, but no paper-positive closure because real corpus retrieval, LLM extraction, stronger baselines, and multi-turn behavior were not directly tested.

## Recommended next action

Run a bounded deepen follow-up on a public fact-verification or QA-with-citations dataset using a stronger retrieval/reranking baseline and threshold calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger loop on a public fact-verification dataset
- Success threshold: At least +5 percentage points absolute accuracy or unsupported-answer reduction versus the stronger baseline, trace-complete rate at least 0.95, and mean CPU latency below 10x the baseline with absolute latency reported.
- Stop condition: Stop if the ledger fails to beat the stronger baseline by 5 absolute points, trace completeness falls below 0.95, or CPU latency exceeds 10x baseline without a corresponding unsupported-answer reduction.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-on-cpu-1e2d770f944c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
