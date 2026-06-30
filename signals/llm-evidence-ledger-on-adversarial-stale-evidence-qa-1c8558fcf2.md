# LLM Evidence Ledger on Adversarial Stale-Evidence QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-evidence-ledger-on-adversarial-stale-evidence-qa-1c8558fcf2`
Run ID: `llm-evidence-ledger-on-adversarial-stale-evidence-qa-1c8558fcf2-20260605T134705141953+0000`

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

- Parent run decision: Agent Reliability via Evidence Ledger: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-22bcef5c1581/runs/agent-reliability-via-evidence-ledger-22bcef5c1581-20260605T083550941440+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

The ledger reached 100% accuracy on 400 adversarial stale-evidence cases, beating the best non-ledger baseline by 77.5 percentage points with a bootstrap 90% delta interval of [74.0, 81.0] percentage points. Across 5 seeds, the advantage appeared once stale adversarial repeats reached 2 or more and vanished when simpler baselines already had enough signal.

## Boundaries and scale limits

400-case main synthetic benchmark plus 25 sweep runs; no live LLM, no natural corpus, no retrieval noise, and no ambiguous or missing validity metadata. This is mechanism evidence, not publication-grade LLM evidence.

## Claim scope

In a deterministic controlled QA benchmark with explicit validity metadata, an evidence-ledger policy that filters evidence by valid_from/valid_to before source-weighted aggregation resisted adversarial stale evidence better than first-seen, majority, confidence-text, recency-only, source-only, and no-validity-ledger baselines.

## Why it stopped

Closed as no-paper useful signal because the controlled mechanism test met its Tier 1 threshold, but no live LLM or naturalistic retrieval evaluation was performed.

## Recommended next action

Run a bounded LLM prompt-level follow-up using the same hidden-label stale-evidence QA cases, comparing normal QA prompting, ledger prompting, and ledger postprocessing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-Level LLM Evidence Ledger on Controlled Stale-Evidence QA
- Success threshold: Ledger prompting or ledger postprocessing must reach at least 90% exact-answer accuracy and improve by at least 20 percentage points over normal QA prompting in adversarial repeat regimes 2, 4, and 8, without losing more than 5 points in repeat regimes 0 and 1.
- Stop condition: Stop if the ledger variant fails to improve over normal QA by 10 percentage points in two or more adversarial regimes, or if model access/dependencies prevent any valid LLM run.

## Evidence references

- Artifact root: `<local-path>/projects/llm-evidence-ledger-on-adversarial-stale-evidence-qa-1c8558fcf2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
