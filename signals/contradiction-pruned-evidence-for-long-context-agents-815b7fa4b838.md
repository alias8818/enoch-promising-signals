# Contradiction-Pruned Evidence for Long Context Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `contradiction-pruned-evidence-for-long-context-agents-815b7fa4b838`
Run ID: `contradiction-pruned-evidence-for-long-context-agents-815b7fa4b838-20260608T023735584404+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/644b992a27af

## What looked useful

Contradiction pruning was most useful as evidence-pack cleaning/compression: budget-4 accuracy tied the best source-aware baselines at 1.000, but retained 0.000 contradictory values versus 1.848 for lexical/source-weighted baselines; at budgets 8 and 16 it stayed at 1.000 accuracy while those baselines dropped to 0.785 and 0.547 mean accuracy.

## Boundaries and scale limits

Synthetic symbolic claims only; no real LLM agent, natural-language NLI, retrieval corpus, multi-hop QA, or transformer long-context behavior was tested. Medium run used 400 cases per condition, 512/2048-claim contexts, and local CPU execution.

## Claim scope

In a deterministic symbolic long-context claim benchmark with source priors and controlled contradictions, source-capped contradiction pruning produced contradiction-free evidence packs with no answer-accuracy loss versus the best source-aware baselines, and avoided higher-budget degradation seen in naive evidence packers.

## Why it stopped

No-paper closure: the result is a controlled symbolic useful signal, not direct evidence for real long-context agents or publication-grade validation.

## Recommended next action

Run a bounded natural-language follow-up with a small LLM or NLI model on contradiction-contaminated long-context QA, measuring answer accuracy, evidence contradiction rate, and token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Contradiction-Pruned Evidence Pack Evaluation
- Success threshold: At matched evidence-token budgets, contradiction pruning reduces contradictory evidence retained by at least 50% while keeping answer accuracy within 2 percentage points of the best baseline, or improves answer accuracy by at least 5 percentage points in high-contradiction settings.
- Stop condition: Stop if contradiction pruning either reduces answer accuracy by more than 5 percentage points without a large evidence-cleanliness gain, or fails to reduce contradictory evidence retained by at least 25% on natural-language cases.

## Evidence references

- Artifact root: `<local-path>/projects/contradiction-pruned-evidence-for-long-context-agents-815b7fa4b838`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
