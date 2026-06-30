# Evidence-Ledger ReAct for Tiny CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-react-for-tiny-cpu-agents-6e557285c228`
Run ID: `evidence-ledger-react-for-tiny-cpu-agents-6e557285c228-20260527T123810822417+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5f787d423580

## What looked useful

Evidence metadata is not free for tiny agents: it hurts versus a compact fact cache under very tight or no-conflict conditions, but helps resolve conflicting evidence once sufficient state budget is available.

## Boundaries and scale limits

No real LLM, no real ReAct tool loop, synthetic templated observations only, single-process CPU execution, 400-task main run plus two 250-task stress checks.

## Claim scope

Synthetic CPU-only memory-state benchmark: evidence-ledger memory improves over raw scratchpad at all tested budgets and over a compact fact cache only when conflicts are common and the budget is large enough to hold provenance.

## Why it stopped

Closed as a proxy useful-signal result, not a full validation: synthetic evidence is mixed and insufficient for a publication-grade claim about ReAct agents.

## Recommended next action

Run a bounded LLM-in-the-loop deepening test with the same raw scratchpad, fact-cache, and evidence-ledger memory policies on small multi-hop QA/tool tasks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop evidence ledger test for tiny CPU ReAct agents
- Success threshold: Evidence ledger beats both controls by at least 10 absolute accuracy points on conflict-heavy tasks without more than 25 percent latency overhead versus fact cache.
- Stop condition: Stop if the ledger fails to beat fact cache by 5 absolute accuracy points in a 100-task pilot or if CPU inference cost exceeds the 15-minute local budget without producing checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-react-for-tiny-cpu-agents-6e557285c228`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
