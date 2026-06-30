# Real-Trace Evidence-Ledger Recovery Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-trace-evidence-ledger-recovery-validation-8a4efdc8eb`
Run ID: `real-trace-evidence-ledger-recovery-validation-8a4efdc8eb-20260529T053923441126+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Streaming Agent Trace Evidence-Ledger Recovery Test: enoch://control-plane/projects/streaming-agent-trace-evidence-ledger-recovery-test-a47b57a566/runs/streaming-agent-trace-evidence-ledger-recovery-test-a47b57a566-20260529T011533891859+0000
- Parent run decision: Real Agent Trace Evidence-Ledger Integration: enoch://control-plane/projects/real-agent-trace-evidence-ledger-integration-495e12b923/runs/real-agent-trace-evidence-ledger-integration-495e12b923-20260528T150914016428+0000

## What looked useful

Segmenting a hash-checked evidence ledger avoids the strict-chain suffix-loss failure mode: middle corruption recovery improved from about 50.0% for strict_chain to 96.8% for segmented_ledger with full detection. Plain JSONL retained high parse recall but failed to detect most integrity failures, including 0% detection for valid JSON payload tampering.

## Boundaries and scale limits

The run used 2k-sample public traces, a local Python prototype, and simulated byte/segment/tamper failures. It did not validate live production ledgers, concurrent writers, real crash timing, full trace corpora, signed external roots, or adversarial manifest rewriting.

## Claim scope

On four public LogHub 2k real trace samples with deterministic simulated file corruptions, a segmented hash-checked evidence ledger recovered intact post-corruption trace evidence with 96.8% mean recall for middle corruption/deletion and 99.2% mean recall for tail truncation while detecting 100% of injected corruptions. This outperformed a strict monolithic hash-chain baseline on recovery and outperformed plain JSONL on corruption detection.

## Why it stopped

Bounded local validation supports the mechanism but remains below publication-grade evidence because failures were simulated and traces were small public samples rather than live/full operational ledgers.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should use full-size real traces or live ledger captures with concurrent writers and signed manifest roots.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live/Full-Trace Segmented Evidence-Ledger Recovery With External Roots
- Success threshold: Segmented ledger achieves >=95% exact recall for non-tail single-region corruption, 100% integrity-failure detection including manifest tamper, <=2.5x storage overhead versus plain JSONL, and no unrecovered clean-run events.
- Stop condition: Stop if full/live traces are unavailable, if signed-root verification cannot be implemented locally, or if segmented recovery recall falls below 90% or misses any integrity tamper in two independent datasets.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-recovery-validation-8a4efdc8eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
