# Operator-model agent memory vs retrieval-only

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-model-agent-memory-vs-retrieval-only-846e10dba6d6`
Run ID: `operator-model-agent-memory-vs-retrieval-only-846e10dba6d6-20260613T033322916669+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfdae30b842d

## What looked useful

Clean exact accuracy was 0.933 for operator memory versus 0.0000116 for strict retrieval and 0.587 for delta retrieval, with 4.07x fewer stored items on average. With 10% corrupted training outputs, operator memory retained 0.922 exact accuracy versus 0.529 for delta retrieval.

## Boundaries and scale limits

Synthetic task only; no LLM agent, no natural-language task distribution, no embedding retrieval corpus, and operator memory used a hand-written candidate program family. Runs were CPU-only local sweeps with 54 operators, 20 seeds per shot count, and 32 tests per operator.

## Claim scope

In a synthetic vector-operator episodic benchmark with known operator names and a candidate rule family containing the true transformations, compact per-operator memory generalized to held-out inputs far better than strict retrieval and a stronger delta-retrieval control.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic and proxy-only for real agent memory, despite supporting the operator-memory mechanism locally.

## Recommended next action

Run a bounded natural-language tool-task follow-up with an actual LLM or lightweight agent comparing schema/operator memory against embedding retrieval under equal storage and token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language tool-task operator memory vs retrieval under equal budget
- Success threshold: Operator/schema memory improves held-out exact task success by at least 10 percentage points over the best retrieval baseline while using no more memory tokens, across at least 10 seeds.
- Stop condition: Stop if embedding retrieval matches or exceeds operator/schema memory under equal budget, or if schema induction fails to exceed retrieval by 5 percentage points after a smoke and medium run.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-agent-memory-vs-retrieval-only-846e10dba6d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
