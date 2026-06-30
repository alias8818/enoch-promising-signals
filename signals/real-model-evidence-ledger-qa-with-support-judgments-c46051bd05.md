# Real-model evidence-ledger QA with support judgments

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-model-evidence-ledger-qa-with-support-judgments-c46051bd05`
Run ID: `real-model-evidence-ledger-qa-with-support-judgments-c46051bd05-20260608T170403413589+0000`

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

- Parent run decision: Evidence Ledger Constrained Agent: enoch://control-plane/projects/evidence-ledger-constrained-agent-8fd94bb76acc/runs/evidence-ledger-constrained-agent-8fd94bb76acc-20260608T142935155064+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e6366c2e2979

## What looked useful

The same model can fabricate an evidence-ledger entry, mark the answer SUPPORTED, and produce an unsupported final answer. Self-generated support judgments alone are therefore not a reliable guardrail in this bounded test.

## Boundaries and scale limits

Single model, small synthetic controlled documents, 20 cases, greedy decoding, automated exact/numeric/abstention scoring; no long-context, retrieval, human grading, multi-model, or externally verified quote-span validation.

## Claim scope

On a 20-case controlled short-document QA test with cached Qwen/Qwen2.5-3B-Instruct, an evidence-ledger plus self-generated support-judgment prompt did not improve grounded QA over a plain answer-only prompt and introduced one fabricated-evidence unanswerable failure.

## Why it stopped

Tier 1 direct test completed; result is a useful no-paper negative signal rather than publication-grade support.

## Recommended next action

Run a bounded deepen follow-up that requires exact quote-span extraction and independent quote verification before support judgments are accepted.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quote-verified evidence ledger QA with independent support checking
- Success threshold: Quote-verified ledger condition matches or exceeds plain baseline overall accuracy, improves or matches unanswerable abstention, preserves at least 95% answerable accuracy, and has zero fabricated ledger entries.
- Stop condition: Stop as unsupported if any fabricated ledger entry passes verification or if the quote-verified ledger condition underperforms the plain baseline on unanswerable abstention by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-evidence-ledger-qa-with-support-judgments-c46051bd05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
