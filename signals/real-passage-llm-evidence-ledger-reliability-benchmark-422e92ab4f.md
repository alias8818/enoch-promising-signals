# Real-passage LLM evidence-ledger reliability benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-passage-llm-evidence-ledger-reliability-benchmark-422e92ab4f`
Run ID: `real-passage-llm-evidence-ledger-reliability-benchmark-422e92ab4f-20260605T115441327036+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence Ledger Agent Reliability with Bounded Falsification: enoch://control-plane/projects/evidence-ledger-agent-reliability-with-bounded-falsification-c178bbda9bef/runs/evidence-ledger-agent-reliability-with-bounded-falsification-c178bbda9bef-20260605T051251017562+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb58a872501e

## What looked useful

A simple exact-copy evidence-ledger benchmark can expose that a model may retain good passage QA accuracy while failing to produce reliable inspectable evidence. Direct QA F1 was 0.9325; best ledger F1 was 0.8329, nonempty evidence 0.400, exact-supported all-quote rate 0.250; oracle gold-span verifier support rate was 1.0.

## Boundaries and scale limits

Single small seq2seq instruction model, 40 passages from one QA dataset, greedy decoding, no constrained JSON decoding, no larger chat-tuned decoder model, no multi-domain benchmark.

## Claim scope

On 40 real SQuAD validation passages with google/flan-t5-base, evidence-ledger prompting did not meet a minimal reliability threshold: zero-shot produced no evidence quotes, and one-example few-shot produced nonempty evidence on 40% of examples with only 25% exact copied answer-supporting ledgers.

## Why it stopped

Tier 1 real-passage direct test failed the stated evidence-ledger reliability threshold; this is an early falsification for the tested model/prompt setting, not a broad full-scale validation.

## Recommended next action

Run a bounded deepen follow-up on a stronger chat-tuned decoder with the same exact-copy verifier and success threshold; stop this run as an early direct falsification for google/flan-t5-base rather than a full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Chat-tuned decoder evidence-ledger reliability on real passages
- Success threshold: Evidence-ledger condition has at least 70% nonempty evidence and at least 70% exact-supported all-quote rate while mean F1 is no more than 10 percentage points below direct-answer prompting.
- Stop condition: Stop if the model produces less than 50% nonempty evidence or less than 50% exact-supported all-quote rate on the first 50 examples, or if malformed ledgers dominate outputs despite one few-shot formatting example.

## Evidence references

- Artifact root: `<local-path>/projects/real-passage-llm-evidence-ledger-reliability-benchmark-422e92ab4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
