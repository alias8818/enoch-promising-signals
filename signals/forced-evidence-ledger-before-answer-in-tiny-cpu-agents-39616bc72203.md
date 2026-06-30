# Forced Evidence Ledger Before Answer in Tiny CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `forced-evidence-ledger-before-answer-in-tiny-cpu-agents-39616bc72203`
Run ID: `forced-evidence-ledger-before-answer-in-tiny-cpu-agents-39616bc72203-20260609T215342084877+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4890047f9ba5

## What looked useful

Across 5,000 confirmation examples at retrieval miss_rate=0.08, forced pre-ledger achieved accuracy 0.8028, coverage 0.8028, and unsupported answer rate 0.0000. Direct answering had accuracy 0.3684 and unsupported answer rate 0.9474; post-hoc ledger had accuracy 0.3632 and unsupported answer rate 0.6684. Sensitivity runs at miss_rate 0.00 and 0.25 preserved zero unsupported answers for forced pre-ledger while coverage fell with retrieval quality.

## Boundaries and scale limits

Synthetic generated facts only; no pretrained LLM, no open-domain retrieval, no multi-hop reasoning, no human evaluation, and no adversarial citation fabrication test. Results should not be generalized to real LLM agents without direct model evidence.

## Claim scope

In a deterministic synthetic single-hop fact QA scaffold with hand-coded tiny CPU policies, forcing evidence retrieval and ledger construction before the final answer eliminates unsupported non-abstained answers and improves accuracy relative to direct answering and post-hoc ledger attachment.

## Why it stopped

Synthetic scaffold evidence supports the mechanism but is not direct evidence about real tiny LLM agents or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete step is a bounded small-LLM replication with automatic citation entailment checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM Pre-Ledger Citation-Gated QA Replication
- Success threshold: Forced pre-ledger reduces unsupported answer rate by at least 25 percentage points versus post-hoc ledger while losing no more than 25 percentage points of coverage, with citation fabrication below 5% on the audited/checkable subset.
- Stop condition: Stop if the small model cannot reliably follow ledger-before-answer formatting, fabricates citations above 20%, or the unsupported-answer reduction is below 10 percentage points versus post-hoc ledger.

## Evidence references

- Artifact root: `<local-path>/projects/forced-evidence-ledger-before-answer-in-tiny-cpu-agents-39616bc72203`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
