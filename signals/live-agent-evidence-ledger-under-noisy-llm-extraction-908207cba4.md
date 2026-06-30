# Live-agent evidence ledger under noisy LLM extraction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-agent-evidence-ledger-under-noisy-llm-extraction-908207cba4`
Run ID: `live-agent-evidence-ledger-under-noisy-llm-extraction-908207cba4-20260609T092622493233+0000`

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

- Parent run decision: Agent Evidence Ledger with Compressed State: enoch://control-plane/projects/agent-evidence-ledger-with-compressed-state-576daac6076c/runs/agent-evidence-ledger-with-compressed-state-576daac6076c-20260609T054402296474+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/df7ee48e93fd

## What looked useful

The ledger mechanism raised moderate-noise provenance accuracy from 0.7654 to 0.9469 and cut wrong fields per case from 0.7415 to 0.1958, but F1 dropped from 0.8575 to 0.7377 and recall dropped from 0.8455 to 0.6262 due to abstention. A relaxed ablation still trailed last-write F1 at 0.7597.

## Boundaries and scale limits

Tier 1 CPU-only synthetic benchmark: 3 noise settings, 20 seeds per setting, 200 cases per seed, 6 fields per case, stochastic extractor instead of real LLM extraction, synthetic structured snippets instead of natural documents, no full tool-using agent re-query loop.

## Claim scope

In a controlled synthetic live-extraction stream with known ground truth, the tested source-aware evidence ledger improved provenance accuracy and reduced wrong facts, but failed the predeclared F1 and recall thresholds against last-write and majority baselines.

## Why it stopped

Controlled Tier 1 direct test failed the predeclared F1 improvement and recall thresholds; this is an early synthetic falsification of the naive ledger decision rule, not a full real-LLM validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should add coverage-aware re-query or retrieval on ledger abstentions and measure whether recall can be recovered while retaining provenance gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-aware ledger re-query for noisy LLM extraction
- Success threshold: On the moderate-noise condition, coverage-aware ledger F1 is at least 0.05 above last-write, provenance accuracy is at least 0.10 above last-write, recall is at least 0.80, and extra extraction calls are below 2x baseline.
- Stop condition: Stop if recall remains below 0.80 or F1 remains below last-write after adding targeted re-query, because the ledger mechanism would still be trading away too much task completion for provenance.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-evidence-ledger-under-noisy-llm-extraction-908207cba4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
