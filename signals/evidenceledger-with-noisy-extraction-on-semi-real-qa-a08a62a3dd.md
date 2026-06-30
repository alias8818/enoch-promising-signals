# EvidenceLedger with Noisy Extraction on Semi-Real QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidenceledger-with-noisy-extraction-on-semi-real-qa-a08a62a3dd`
Run ID: `evidenceledger-with-noisy-extraction-on-semi-real-qa-a08a62a3dd-20260604T015543996558+0000`

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

- Parent run decision: EvidenceLedger_SmallAgent_CPU: enoch://control-plane/projects/evidenceledger-smallagent-cpu-271fe41e7d7a/runs/evidenceledger-smallagent-cpu-271fe41e7d7a-20260603T211251123169+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7dfe5b51a415

## What looked useful

Ledger accuracy ranged from 0.8800 to 0.9967 versus majority baseline 0.6300 to 0.9633 and highest-confidence baseline 0.3633 to 0.7200. Bootstrap 90% intervals for ledger minus majority were positive in all six conditions, with lower bounds from +0.0167 to +0.2067.

## Boundaries and scale limits

The extraction layer was simulated; no real LLM/IE extractor, no human citation labeling, no multi-dataset robustness, and no adversarially generated citations were tested. The result supports a mechanism but is not end-to-end QA or publication-grade validation.

## Claim scope

On 300 real SQuAD dev QA examples with simulated noisy extraction traces and citation provenance, EvidenceLedger scoring by context-backed citation support plus corroboration improved exact-answer selection over highest-confidence and majority baselines in all six tested noise conditions.

## Why it stopped

Tier 1 direct controlled test completed; result is a useful mechanism signal but not paper-positive because the noisy extractor was simulated.

## Recommended next action

Run the same ledger-vs-baseline protocol on traces from a real extractor or LLM over held-out QA examples with citation labels; do not write a paper from this simulated-extraction result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: EvidenceLedger on Real Extractor Traces for Semi-Real QA
- Success threshold: EvidenceLedger minus majority exact-match accuracy bootstrap 90% lower bound greater than +0.02 on real extractor traces, with no evidence that gains come only from answer-normalization artifacts.
- Stop condition: Stop as negative/no-paper if the bootstrap 90% lower bound for EvidenceLedger minus majority is <= 0 or if manual audit shows the ledger exploits synthetic or invalid citation labels rather than real provenance.

## Evidence references

- Artifact root: `<local-path>/projects/evidenceledger-with-noisy-extraction-on-semi-real-qa-a08a62a3dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
