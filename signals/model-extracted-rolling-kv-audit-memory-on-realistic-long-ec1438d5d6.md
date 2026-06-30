# Model-extracted rolling KV audit memory on realistic long-session transcripts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `model-extracted-rolling-kv-audit-memory-on-realistic-long-ec1438d5d6`
Run ID: `model-extracted-rolling-kv-audit-memory-on-realistic-long-ec1438d5d6-20260526T233901202945+0000`

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

- Parent run decision: Rolling KV-Compressed Evidence Summary for Long Session Audit: enoch://control-plane/projects/rolling-kv-compressed-evidence-summary-for-long-session-audit-3f3c4474f270/runs/rolling-kv-compressed-evidence-summary-for-long-session-audit-3f3c4474f270-20260525T021650875184+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

Prompt-only model extraction preserved some facts outside a 24-line recency window, but final audit-valid accuracy was 10/24 (41.67%), below the 70% Tier 1 threshold and worse than a 36-line recency oracle. Failures were systematic for stale overwrites, negative mentions, missed updates, and malformed/invalid updates.

## Boundaries and scale limits

Synthetic realistic transcripts only; two sessions and 24 slot queries; one local 2.4 GB GGUF model; no production transcripts, multi-day logs, constrained decoding, larger models, or human semantic grading.

## Claim scope

Two controlled generated realistic long-session transcripts tested local Phi-4-mini chunk-by-chunk extraction into rolling KV memory with line-cited audit evidence.

## Why it stopped

Controlled small direct test falsified the current prompt-only rolling KV audit-memory implementation against the 70% audit-valid threshold; this is not a full validation of the broad idea.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up using schema-constrained extraction plus per-slot evidence verification on the same harness and additional transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Schema-constrained rolling KV audit memory with evidence verification
- Success threshold: At least 70% audit-valid accuracy, at least 25 percentage-point improvement over both recency controls, invalid update rate below 5%, and no repeated stale-overwrite failure across slots.
- Stop condition: Stop if audit-valid accuracy remains below 60% after constrained decoding and evidence verification, or if stale-overwrite errors remain present in both held-out sessions.

## Evidence references

- Artifact root: `<local-path>/projects/model-extracted-rolling-kv-audit-memory-on-realistic-long-ec1438d5d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
