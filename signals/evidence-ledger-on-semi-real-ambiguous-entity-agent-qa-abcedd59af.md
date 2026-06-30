# Evidence ledger on semi-real ambiguous-entity agent QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-semi-real-ambiguous-entity-agent-qa-abcedd59af`
Run ID: `evidence-ledger-on-semi-real-ambiguous-entity-agent-qa-abcedd59af-20260607T201212681089+0000`

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

- Parent run decision: Tiny CPU Agent Evidence Ledger: enoch://control-plane/projects/tiny-cpu-agent-evidence-ledger-94882e94540e/runs/tiny-cpu-agent-evidence-ledger-94882e94540e-20260607T161009722547+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3b211a9fba

## What looked useful

The evidence ledger improved controlled ambiguous-entity QA from 0.8611 to 1.0000 accuracy, citation sufficiency from 0.5000 to 1.0000, and ambiguous abstention accuracy from 0.0000 to 1.0000 on the saved harness. This supports the mechanism but is not paper-positive.

## Boundaries and scale limits

The corpus and questions are locally generated semi-real records, not independently labeled live web evidence. The QA policy is deterministic rather than an LLM/tool-using agent. Results do not establish robustness to larger corpora, paraphrase, stale evidence, adversarial retrieval noise, or production agent behavior.

## Claim scope

In a deterministic Tier 1 semi-real ambiguous-entity QA harness with 26 evidence documents, 8 ambiguous entity records, and 36 questions, an entity-keyed evidence ledger achieved perfect exact-answer accuracy, citation sufficiency, and unresolved-ambiguity abstention while a retrieval-only baseline failed the abstention and citation-provenance checks.

## Why it stopped

Tier 1 controlled direct test met the scoped mechanism threshold, but evidence remains small, semi-synthetic, and deterministic; finalize as no-paper useful signal rather than paper-positive.

## Recommended next action

Run a bounded LLM/tool-agent evaluation on independently labeled real ambiguous entities, requiring the ledger agent to improve citation sufficiency and unresolved-ambiguity abstention without reducing exact-answer accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent evidence ledger test on real ambiguous entities
- Success threshold: Ledger agent improves citation sufficiency by at least 20 percentage points and unresolved-ambiguity abstention by at least 30 percentage points, with exact-answer accuracy no worse than retrieval-only by more than 2 percentage points on at least 100 questions.
- Stop condition: Stop if the ledger agent fails to improve either citation sufficiency or unresolved-ambiguity abstention, or if exact-answer accuracy drops by more than 2 percentage points versus retrieval-only.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-semi-real-ambiguous-entity-agent-qa-abcedd59af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
