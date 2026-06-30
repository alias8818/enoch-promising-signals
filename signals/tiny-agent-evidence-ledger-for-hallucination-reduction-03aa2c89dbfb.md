# Tiny Agent Evidence Ledger for Hallucination Reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-hallucination-reduction-03aa2c89dbfb`
Run ID: `tiny-agent-evidence-ledger-for-hallucination-reduction-03aa2c89dbfb-20260607T210025522980+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Across 360 synthetic condition runs, baseline unsupported answer rate averaged 0.6050 while the evidence-ledger agent averaged 0.0; ledger abstention averaged 0.2796 and false answers on unanswerable queries fell from 1.0 to 0.0.

## Boundaries and scale limits

Synthetic world only; no real LLM, no real retrieval corpus, no ambiguous natural-language evidence extraction, and no production hallucination benchmark. Full sweep was CPU-only with 40 seeds and 160 synthetic entities per condition.

## Claim scope

In a deterministic synthetic QA proxy, a tiny agent that only emits answers bound to retrieved evidence eliminated unsupported emitted answers relative to a noisy-prior baseline, while abstaining on evidence-missing queries.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct evidence of real LLM hallucination reduction or paper-ready robustness.

## Recommended next action

Run a bounded direct follow-up on a real small QA benchmark with a local or API LLM, adversarial unanswerable questions, shared retrieval, and answer-evidence support scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger on real QA passages with adversarial unanswerables
- Success threshold: Unsupported emitted answer rate reduced by >=50% relative to baseline with <=10 percentage point loss in answerable-question accuracy.
- Stop condition: Stop if the ledger reduces unsupported answers by <20%, if accuracy loss exceeds 15 percentage points, or if support labels are too unreliable to score.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-hallucination-reduction-03aa2c89dbfb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
