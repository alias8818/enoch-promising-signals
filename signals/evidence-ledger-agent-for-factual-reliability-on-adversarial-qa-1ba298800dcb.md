# Evidence-Ledger Agent for Factual Reliability on Adversarial QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-for-factual-reliability-on-adversarial-qa-1ba298800dcb`
Run ID: `evidence-ledger-agent-for-factual-reliability-on-adversarial-qa-1ba298800dcb-20260619T224940145115+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Explicit evidence ledgering with conservative abstention can eliminate tested lexical distractor, outdated conflict, equal conflict, and unsupported-query failures in a controlled benchmark.

## Boundaries and scale limits

No real open-domain retrieval, LLM generation, noisy extraction, human-labeled benchmark, or strong RAG baseline was tested. The result supports the mechanism only in a controlled synthetic setting.

## Claim scope

On a deterministic synthetic adversarial QA benchmark with templated source snippets, an evidence-ledger policy that records subject-relation-object claims, source reliability, recency, and conflict state achieved 100% accuracy across 20 seeded 100-item runs, compared with 21%-25% for a lexical retrieval baseline.

## Why it stopped

Synthetic local evidence is useful but insufficient for a paper-positive decision; this is not a full validation of factual reliability on adversarial QA.

## Recommended next action

Run a bounded real-data follow-up on adversarial factual QA with retrieved passages, noisy extraction, and a modern RAG/LLM baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Data Evidence-Ledger QA Validation
- Success threshold: At least +10 percentage-point reliability improvement or statistically significant unsupported-answer reduction versus the best baseline, while preserving a predeclared minimum answer coverage.
- Stop condition: Stop if extraction noise eliminates the reliability gain or if ledger abstention only improves accuracy by refusing too many answerable questions.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-factual-reliability-on-adversarial-qa-1ba298800dcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
