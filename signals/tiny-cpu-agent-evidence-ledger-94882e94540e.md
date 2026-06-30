# Tiny CPU Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-cpu-agent-evidence-ledger-94882e94540e`
Run ID: `tiny-cpu-agent-evidence-ledger-94882e94540e-20260607T161009722547+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3b211a9fba

## What looked useful

The ledger held unsupported_rate at 0.0 across all tested distractor levels. The baseline unsupported_rate rose from 0.442 with 1 distractor to 0.764 with 8 distractors. Ledger coverage fell to 0.811 at 4 distractors and 0.444 at 8 distractors with k=4, then improved to 1.000 and 0.894 respectively with k=8, showing a grounding-versus-abstention tradeoff tied to retrieval budget.

## Boundaries and scale limits

Synthetic documents only; deterministic rule agents only; no real LLM, real corpus, long-horizon autonomy, adversarial evidence, or human evaluation. Main benchmark used 1000 tasks per distractor level and k=4, plus a k=8 retrieval-budget check for 4 and 8 distractors.

## Claim scope

On deterministic synthetic subject-fact QA tasks with near-name distractors, an exact subject-linked evidence ledger prevents unsupported emitted facts compared with a naive lexical retrieve-and-fill tiny CPU agent, at negligible CPU cost, but may abstain when exact evidence falls outside top-k retrieval.

## Why it stopped

Proxy mechanism test completed with useful signal but insufficient direct evidence for real agent behavior or publication-grade claims.

## Recommended next action

Stop this proxy run; deepen with a bounded semi-real corpus and a local small LLM or stronger retrieval baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger on semi-real ambiguous-entity agent QA
- Success threshold: Ledger unsupported_rate at least 50% lower than baseline with coverage >= 0.80 and mean per-task CPU latency overhead <= 25% on at least 200 human-inspectable tasks.
- Stop condition: Stop if ledger coverage remains below 0.60 at practical retrieval budgets or unsupported_rate is not reduced by at least 25% versus the stronger baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-agent-evidence-ledger-94882e94540e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
