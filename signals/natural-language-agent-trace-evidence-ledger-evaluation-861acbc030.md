# Natural-Language Agent Trace Evidence Ledger Evaluation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-agent-trace-evidence-ledger-evaluation-861acbc030`
Run ID: `natural-language-agent-trace-evidence-ledger-evaluation-861acbc030-20260612T094935889192+0000`

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

- Parent run decision: Evidence-Ledger Compressed Long-Horizon Agent Context: enoch://control-plane/projects/evidence-ledger-compressed-long-horizon-agent-context-65b105219361/runs/evidence-ledger-compressed-long-horizon-agent-context-65b105219361-20260611T144058986306+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Structured evidence ledgers can verify claims and preserve citations when agent traces use stable evidence syntax, but brittle extraction makes the approach insufficient for natural-language trace robustness without a stronger parser or extractor.

## Boundaries and scale limits

Synthetic controlled traces only; no real production traces, no messy open-domain claim segmentation, no LLM extraction, no human audit study, and no broad robustness validation.

## Claim scope

On 60 controlled schema-like natural-language traces with 180 seeded final-answer claims, a deterministic evidence ledger caught contradicted or missing claims with F1 1.00 and citation accuracy 1.00, beating a raw keyword baseline by 0.333 F1. On an equally sized paraphrased format-shift condition, the same ledger failed the success threshold with 0.00 citation accuracy and no F1 gain over baseline.

## Why it stopped

Tier 1 direct controlled evidence is mixed: canonical syntax supports the mechanism, but modest natural-language format shift fails the citation and baseline-gain thresholds, so this is no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded deepen test on paraphrased traces using a robust extraction layer and require citation-preserving verification to clear the same threshold before considering larger real-trace validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Citation-preserving robust extraction for paraphrased agent trace ledgers
- Success threshold: On paraphrased traces, ledger bad-claim F1 >= 0.85, F1 gain over raw keyword baseline >= 0.20, exact status accuracy >= 0.85, and contradiction citation accuracy >= 0.90.
- Stop condition: Stop if citation accuracy remains below 0.75 or exact status accuracy remains below 0.75 on the paraphrased controlled set after one robust extraction implementation.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-agent-trace-evidence-ledger-evaluation-861acbc030`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
