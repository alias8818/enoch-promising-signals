# Direct LLM Evidence-Ledger QA Reliability Test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-llm-evidence-ledger-qa-reliability-test-28d290244c`
Run ID: `direct-llm-evidence-ledger-qa-reliability-test-28d290244c-20260621T142534280292+0000`

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

- Parent run decision: Structured Evidence-Ledger Agent Reliability Probe: enoch://control-plane/projects/structured-evidence-ledger-agent-reliability-probe-389256032822/runs/structured-evidence-ledger-agent-reliability-probe-389256032822-20260621T141450097517+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14825ec65079

## What looked useful

Ledger prompting reduced accuracy from 0.8667 to 0.8000 and increased unsupported-answer rate from 0.1333 to 0.2000. It was especially worse on unanswerable questions, while citation compliance was weak with only 0.5333 expected citation rate and 0.1000 spurious citation rate.

## Boundaries and scale limits

Single cached 1.5B instruction model; small synthetic evidence packets; no naturalistic documents, multi-model replication, constrained JSON decoder, long-context retrieval, or adversarial benchmark.

## Claim scope

In a 30-case controlled synthetic QA test using Qwen/Qwen2.5-1.5B-Instruct with deterministic decoding, an explicit evidence-ledger prompt did not improve answer reliability over a raw-context prompt.

## Why it stopped

Tier 1 direct small test falsified the preregistered improvement threshold for this model/prompt setup: ledger accuracy was lower and unsupported-answer rate was higher than raw context, so this is a no-paper useful signal rather than a paper-positive result.

## Recommended next action

Run one bounded deepen follow-up with constrained JSON/canonical evidence-ID decoding on the same benchmark plus a second small instruction model; stop if answer accuracy and unsupported-answer rate still fail to beat raw context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained Evidence-ID Ledger QA Reliability Check
- Success threshold: Ledger mode must beat raw-context mode by at least 10 percentage points in accuracy, have a lower unsupported-answer rate, and achieve at least 0.90 valid expected citation rate with zero malformed evidence IDs.
- Stop condition: Stop as unsupported if constrained ledger mode does not beat raw context on both accuracy and unsupported-answer rate on the controlled benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-evidence-ledger-qa-reliability-test-28d290244c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
