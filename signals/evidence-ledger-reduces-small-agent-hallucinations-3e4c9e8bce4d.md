# Evidence ledger reduces small agent hallucinations

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-reduces-small-agent-hallucinations-3e4c9e8bce4d`
Run ID: `evidence-ledger-reduces-small-agent-hallucinations-3e4c9e8bce4d-20260607T142749037252+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ec992d4816f3

## What looked useful

Corrected scoring found zero substantive unsupported answers in both baseline and ledger conditions. The ledger improved citation validity from 0.7708 to 0.9375 but increased mean latency from 0.723s to 3.102s, so the primary hallucination-reduction claim was unsupported under a fair abstention baseline.

## Boundaries and scale limits

Short synthetic snippets only; 24 answerable and 24 unanswerable items; one stable local model; no real retrieval corpus, web/tool agent, multi-step workflow, or multi-model robustness validation.

## Claim scope

On a 48-item synthetic document-grounded QA benchmark using local Qwen2.5-7B-Instruct Q4_K_M, an evidence-ledger prompt did not reduce substantive unsupported answers relative to a strong baseline prompt that already explicitly required abstention.

## Why it stopped

Bounded local direct test found no hallucination reduction because the strong baseline already abstained on all unanswerable items; this is not full validation, but it is an early negative against the primary claim as tested.

## Recommended next action

Stop this run as a useful negative; a bounded follow-up should test harder real or adversarial document-QA tasks where a strong abstention baseline has measurable substantive unsupported answers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger on harder abstention-resistant document QA
- Success threshold: Ledger reduces substantive unsupported-answer rate by at least 30% relative with supported accuracy loss no greater than 5 percentage points and mean latency no more than 5x baseline.
- Stop condition: Stop if the strong baseline again has under 5% substantive unsupported answers, or if ledger gains come only from over-abstention that drops supported accuracy by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-small-agent-hallucinations-3e4c9e8bce4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
