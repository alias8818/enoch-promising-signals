# Compressed Evidence Ledger for Small CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-evidence-ledger-for-small-cpu-agents-13abb2990ffa`
Run ID: `compressed-evidence-ledger-for-small-cpu-agents-13abb2990ffa-20260526T011811037896+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

Compressed tuple ledgers can preserve conflict history, provenance, and tamper-audit utility that a lossy rolling summary drops, while reducing in-context memory by 79.4% versus raw notes in this benchmark.

## Boundaries and scale limits

Synthetic evidence with perfect field extraction; no real web documents, no LLM extraction errors, no multi-turn agent planning, no human trust evaluation, and no long-horizon context drift. Offline zlib compression favored repetitive raw text, so the supported compression claim is limited to active context footprint.

## Claim scope

On a deterministic synthetic benchmark with 5 seeds, 600 evidence snippets per seed, and structured model-evaluation facts, a normalized compressed tuple ledger preserved raw-note answer accuracy, provenance F1, and hash audit behavior while using 20.6% of raw approximate context tokens.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct real-agent evidence sufficient for a paper.

## Recommended next action

Run a bounded deepen follow-up on real noisy documents with a local extractor or small LLM, comparing raw notes, tuple ledger, and rolling summaries on task answers, provenance, extraction failures, and context cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-document compressed evidence ledger validation for small CPU agents
- Success threshold: Compressed ledger reaches at least 95% of raw-note answer accuracy and provenance F1, at least 90% conflict recall, clean audit pass of 1.0, tamper detection matching raw hash notes, and at least 50% active-token reduction.
- Stop condition: Stop as unsupported if extraction noise drops compressed-ledger answer accuracy or provenance F1 below 90% of raw notes, conflict recall below 80%, or token reduction below 30%.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-for-small-cpu-agents-13abb2990ffa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
