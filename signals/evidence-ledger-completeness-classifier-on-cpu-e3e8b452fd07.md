# Evidence-Ledger Completeness Classifier on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-completeness-classifier-on-cpu-e3e8b452fd07`
Run ID: `evidence-ledger-completeness-classifier-on-cpu-e3e8b452fd07-20260610T193030310119+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

The full-feature logistic classifier reached test F1 0.9995 with 1 false positive and 0 false negatives, and OOD F1 0.9940 with 12 false positives and 0 false negatives. Baselines were much weaker: majority OOD F1 0.6627, count-only OOD F1 0.6767, and three-feature rule OOD F1 0.8002. Removing issue-specific features dropped OOD F1 to 0.8477, supporting the mechanism that contradiction/staleness/mismatch/orphan features carry useful completeness signal.

## Boundaries and scale limits

Synthetic-only proxy; no real human-written ledgers, no LLM extraction pipeline, no adversarial paraphrases, no production latency integration, and no external benchmark labels were tested.

## Claim scope

On a controlled synthetic corpus of structured evidence ledgers, a lightweight CPU logistic classifier using completeness-specific features detects incomplete ledgers far better than majority, count-only, and three-feature baselines, including an OOD split with larger ledgers and an unseen orphan-claim corruption type.

## Why it stopped

Evidence supports the bounded synthetic mechanism but is not direct real-world validation and therefore is not publication-grade.

## Recommended next action

Stop this run as a synthetic no-paper useful signal; next test should evaluate the same feature set on a small real or human-audited evidence-ledger corpus before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Ledger Completeness Classifier Validation
- Success threshold: Full-feature classifier F1 >= 0.85 and at least 0.10 absolute F1 improvement over the strongest simple baseline on held-out real/audited ledgers.
- Stop condition: Stop as unsupported if held-out F1 is below 0.75 or does not beat the strongest simple baseline by at least 0.05 F1.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-completeness-classifier-on-cpu-e3e8b452fd07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
