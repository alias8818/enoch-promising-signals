# Falsifiable Evidence-Ledger Test for Small Agent Reports

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiable-evidence-ledger-test-for-small-agent-reports-02546c254139`
Run ID: `falsifiable-evidence-ledger-test-for-small-agent-reports-02546c254139-20260611T183912744308+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ec5fc68e5ade

## What looked useful

Claim-level ledgers with source ids, hashes, spans, and support text are mechanically falsifiable and beat a weak keyword-overlap audit, but this setup is too easy: exact sentence matching without a ledger ties the ledger at 1.000 recall and 0.000 false-positive rate while the ledger adds about 3.16x character overhead.

## Boundaries and scale limits

Synthetic CPU-only benchmark; supported claims are exact evidence sentence copies; no real agent reports, paraphrases, multi-hop claims, human review timing, or LLM-generated ledgers were tested.

## Claim scope

In a deterministic synthetic benchmark of 1000 short exact-copy reports with 6000 sentence-level claims, an evidence-ledger auditor caught all injected unsupported entity/unit/region/year/value corruptions, but an exact-text plain-report baseline achieved the same recall and false-positive rate.

## Why it stopped

Bounded synthetic evidence supports the ledger mechanism but does not show an advantage over a strong exact-text plain-report control; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on paraphrased and multi-hop small agent reports with a strong semantic non-ledger auditor baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paraphrased Small-Report Evidence Ledger Benchmark
- Success threshold: Ledger auditor improves unsupported-claim recall or localization by at least 10 percentage points over the strongest non-ledger baseline while keeping false-positive rate <= 0.05 and overhead <= 3.5x.
- Stop condition: Stop if exact or semantic non-ledger baselines match ledger recall/localization within 2 percentage points or if ledger overhead exceeds 3.5x without a detection/localization gain.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-test-for-small-agent-reports-02546c254139`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
