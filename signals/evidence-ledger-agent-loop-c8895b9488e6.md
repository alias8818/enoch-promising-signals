# Evidence-Ledger Agent Loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-c8895b9488e6`
Run ID: `evidence-ledger-agent-loop-c8895b9488e6-20260522T135234636955+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

Across 22,500 grid cases, the ledger loop reduced unsupported and contradicted claims from 1.0119 per case to 0 while improving mean accuracy from 0.4940 to 1.0. In 4,500 same-rank trusted-conflict stress cases, it reduced unsupported and contradicted claims from 0.7013 per case to 0 by abstaining on 27.96% of cases.

## Boundaries and scale limits

Synthetic records only; no LLM, no natural-language extraction, no real retrieval corpus, no human-labeled benchmark, and no long-horizon deployed agent workload. Results should not be treated as publication-grade evidence for real LLM agents.

## Claim scope

In a deterministic synthetic retrieval task with explicit trust and currentness metadata, an append-only evidence ledger plus final claim-support gate reduces unsupported and contradicted answers versus a stop-early scratchpad baseline, with millisecond-scale overhead.

## Why it stopped

No-paper closure: the current evidence is a synthetic mechanism probe, not a direct validation on real LLM agents or real corpora.

## Recommended next action

Run a bounded LLM/tool-agent deepen test on a public grounded-QA or compliance-style benchmark using the same ledger gate and a same-model no-ledger baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Tool-Agent Evidence Ledger Grounding Test
- Success threshold: Ledger agent reduces unsupported or contradicted claims by at least 30% relative to the no-ledger baseline, with no more than a 10 percentage-point accuracy loss and less than 2x latency/cost overhead.
- Stop condition: Stop if the ledger does not reduce unsupported or contradicted claims by at least 10% in a 100-example pilot, or if instrumentation overhead exceeds 3x before improving grounding metrics.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-c8895b9488e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
