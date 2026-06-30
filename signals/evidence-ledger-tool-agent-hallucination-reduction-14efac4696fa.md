# Evidence-ledger tool-agent hallucination reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa`
Run ID: `evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa-20260601T035540826753+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/88b7da3728d1

## What looked useful

Across 30 paired seeds of 500 queries, unsupported claim rate fell from 0.1218 to 0.0000 and F1 rose from 0.7895 to 0.8352 under a clean evidence ledger. A 10% corrupt-tool probe kept unsupported rate at 0.0000 but ledger precision was only 0.8982, showing the method does not fix bad tool evidence.

## Boundaries and scale limits

The experiment used synthetic entities, exact fact-id support, single-hop retrieval, and a mock stochastic agent. It did not test real LLM generations, natural-language entailment, prompt-only citation baselines, multi-hop tool traces, human answer quality, or production retrieval/tool failures.

## Claim scope

In a synthetic atomic fact-id benchmark, gating final tool-agent claims to facts recorded in an evidence ledger eliminated unsupported emitted claims from the same generated candidate set and improved precision/F1 without materially changing recall.

## Why it stopped

Synthetic exact-support evidence supports the mechanism but is not direct/full validation of real tool-agent hallucination reduction.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the ledger gate on real LLM tool-agent traces with natural-language claim extraction and entailment-based support checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence-ledger gating for tool-agent claims
- Success threshold: At least 50% relative reduction in unsupported claim rate compared with prompt-only citation baseline, no more than 10% relative recall loss, and no increase in tool-supported false claims on corrupted-evidence cases.
- Stop condition: Stop if claim extraction/support adjudication cannot reach acceptable agreement, or if unsupported-claim reduction is below 25% relative in a 100-trace pilot.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
