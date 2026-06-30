# Semantic Compression for Reusable Operator Doctrine in Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-compression-for-reusable-operator-doctrine-in-agent-memory-d05dff83b217`
Run ID: `semantic-compression-for-reusable-operator-doctrine-in-agent-memory-d05dff83b217-20260621T065842030126+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/c306aceb6219

## What looked useful

Doctrine-level semantic compression achieved 0.7286 mean accuracy across 20 seeds versus 0.0000-0.3753 for full episodic recall under tested budgets, 0.1880-0.1981 for lexical summaries, and 0.1250 for action-only compressed memory, with 60.30x lower stored-token footprint than episodic memory.

## Boundaries and scale limits

Synthetic single-step retrieval proxy only; doctrine groups and canonical compressed rules are hand-authored from known latent classes; no real agent traces, no LLM induction, no live multi-step agent success metric, and no large-scale robustness evaluation.

## Claim scope

In a synthetic eight-doctrine operator-memory benchmark, compact doctrine entries preserved action-relevant retrieval accuracy better than verbose episodic recall under 40-320 token budgets while reducing stored tokens by about 60x.

## Why it stopped

No-paper closure: this run produced a reproducible synthetic useful signal, but it is proxy evidence rather than direct validation of autonomous doctrine induction or live agent performance.

## Recommended next action

Run a bounded deepen follow-up on real agent traces where doctrine is induced automatically, then evaluate retrieved doctrine in a live task loop against episodic, summary, and embedding-retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic Doctrine Induction from Real Agent Traces
- Success threshold: At least 15 percentage-point absolute improvement in held-out task success or correct operator action selection over the strongest non-doctrine baseline at equal token budget, with no increase in destructive or unsafe actions.
- Stop condition: Stop if automatically induced doctrine does not beat the strongest non-doctrine baseline by at least 5 percentage points on a 50-task pilot or if induced doctrine frequently recommends unsafe/destructive actions.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-for-reusable-operator-doctrine-in-agent-memory-d05dff83b217`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
