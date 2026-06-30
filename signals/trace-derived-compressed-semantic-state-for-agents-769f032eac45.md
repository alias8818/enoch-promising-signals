# Trace-Derived Compressed Semantic State for Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-compressed-semantic-state-for-agents-769f032eac45`
Run ID: `trace-derived-compressed-semantic-state-for-agents-769f032eac45-20260621T121304487604+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

The mechanism is useful under slot-fitting budgets but brittle under naive truncation: at 500 and 900 chars compressed state reached 1.000 accuracy, while at 300 chars it fell to 0.375 and lost to transcript search at 0.432.

## Boundaries and scale limits

Synthetic traces, rule-based extraction, 96 replay tasks, 768 questions, one seed, no LLM extraction, no real operator logs, no live agent task-completion measurement, and no robustness study beyond a three-point character-budget sweep.

## Claim scope

On a deterministic synthetic replay benchmark with structured noisy traces, trace-derived compressed semantic state answered current-state questions at 1.000 accuracy once the memory budget could hold all extracted slots, using fewer mean characters than transcript-search and flat-retrieval baselines.

## Why it stopped

Small synthetic mechanism evidence is useful but not direct enough for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up on real or LLM-generated agent traces with imperfect extraction, matched memory budgets, and a slot-prioritization ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed semantic state with imperfect extraction on realistic agent traces
- Success threshold: Compressed semantic state improves accuracy per memory character by at least 15% over the strongest retrieval baseline at two or more matched budgets, without stale-value error rate exceeding 5%.
- Stop condition: Stop if compressed state does not beat the strongest retrieval baseline at any matched budget or if extraction/stale-value errors exceed the retrieval baseline by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-compressed-semantic-state-for-agents-769f032eac45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
