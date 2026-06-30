# Natural-language extraction test for evidence-ledger tiny agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-extraction-test-for-evidence-ledger-tiny-a58d539ed6`
Run ID: `natural-language-extraction-test-for-evidence-ledger-tiny-a58d539ed6-20260530T081459568380+0000`

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

- Parent run decision: Evidence Ledger for Tiny Local Agents: enoch://control-plane/projects/evidence-ledger-for-tiny-local-agents-2b587e5d0911/runs/evidence-ledger-for-tiny-local-agents-2b587e5d0911-20260529T152810937385+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9c7d9b00b62d

## What looked useful

Final compact extractor at 4096 bytes achieved 0.427 exact answer+source accuracy versus 0.154 for rolling notes and 0.427 for oracle structured extraction; extraction precision and recall were both 1.000. The remaining error is storage-budget limited rather than extraction limited.

## Boundaries and scale limits

Five fixed seeds, 80 entities, 1200 generated documents per seed, deterministic templates only, no real LLM/tool traces, no learned extraction, and no arbitrary natural-language paraphrase robustness.

## Claim scope

In a controlled synthetic natural-language evidence stream with fixed templates, distractors, conflicting updates, and byte-budgeted tiny memory, a small deterministic extractor can recover all generated facts and match an oracle structured-ledger ceiling, but the naive append-row ledger misses the preset 4096-byte exact answer-plus-source accuracy threshold.

## Why it stopped

Controlled Tier 1 direct test produced a useful mechanism signal but failed the preset absolute 4096-byte threshold and remains generator-scoped, so it is not paper-positive.

## Recommended next action

Run a bounded key-aware/latest-fact compaction follow-up at the same 4096-byte budget; stop if it cannot exceed 0.50 exact answer+source accuracy while matching oracle extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Key-aware compaction for natural-language extracted tiny evidence ledgers
- Success threshold: At 4096 bytes, key-aware compact ledger exact answer+source accuracy >= 0.50, delta versus rolling_notes >= 0.15, extraction precision >= 0.98, and extraction recall >= 0.98.
- Stop condition: Stop if key-aware compaction remains below 0.50 exact answer+source accuracy at 4096 bytes or if it only improves by changing the extraction task/generator.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-extraction-test-for-evidence-ledger-tiny-a58d539ed6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
