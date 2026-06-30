# Evidence-ledger gate for agent factual claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gate-for-agent-factual-claims-1a3d0cc0af02`
Run ID: `evidence-ledger-gate-for-agent-factual-claims-1a3d0cc0af02-20260619T091656912995+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/32d194b9714d

## What looked useful

Citation presence passed 82.8% of unsupported/contradicted synthetic claims, while a normalized evidence-ledger gate passed 0.0% of unsupported claims and 100.0% of supported claims. A strict exact-match ledger gate falsely blocked 34.55% of supported paraphrases, showing normalization or NLI is required.

## Boundaries and scale limits

Synthetic templates only; no real LLM outputs, no human-labeled open-domain traces, no retrieval noise, no multi-hop evidence, and no production latency or UX evaluation.

## Claim scope

In a deterministic synthetic benchmark with structured evidence records, atomic claims, contradicted values, irrelevant citations, missing citations, fabricated subjects, and supported relation paraphrases, a normalized evidence-ledger gate blocked unsupported claims better than citation presence while preserving supported claims.

## Why it stopped

Useful synthetic mechanism signal only; not a full validation because the benchmark uses generated templates rather than real agent traces and human factuality labels.

## Recommended next action

Run a bounded real-trace evaluation with 100-300 agent answers, human-labeled atomic claim support, and an NLI-backed ledger comparator before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence-ledger gate evaluation
- Success threshold: Unsupported claim pass rate at least 50% lower than citation-presence baseline and supported false block rate below 10% on human-labeled real traces.
- Stop condition: Stop if the ledger gate fails to beat citation-presence on unsupported pass rate or blocks 10% or more supported claims after one normalization/NLI pass.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gate-for-agent-factual-claims-1a3d0cc0af02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
