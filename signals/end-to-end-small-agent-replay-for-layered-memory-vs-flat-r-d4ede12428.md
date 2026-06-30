# End-to-end small-agent replay for layered memory vs flat retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-small-agent-replay-for-layered-memory-vs-flat-r-d4ede12428`
Run ID: `end-to-end-small-agent-replay-for-layered-memory-vs-flat-r-d4ede12428-20260621T221505020799+0000`

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

- Parent run decision: Layered Operator-Doctrine Memory vs Flat Retrieval for Small Agents: enoch://control-plane/projects/layered-operator-doctrine-memory-vs-flat-retrieval-for-small-agents-94c46710735c/runs/layered-operator-doctrine-memory-vs-flat-retrieval-for-small-agents-94c46710735c-20260621T215403248838+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2852c88656c4

## What looked useful

Layered scoped active-state memory avoided flat top-k blending errors in a small direct replay harness, but a simple transcript-search control solved the same generated tasks, limiting novelty and paper readiness.

## Boundaries and scale limits

Synthetic generated data only; lexical retrieval only; no LLM answer synthesis, human-authored transcripts, embedding store, production persistence, or long-horizon robustness. Transcript top-1 search also reached 100%, so the result is not evidence that layered memory beats all strong flat/transcript baselines.

## Claim scope

In a deterministic Tier 1 synthetic repeated-agent replay with 2560 scoped fact queries, layered active-state doctrine/profile memory beat the implemented flat top-k retrieval aggregation baseline by 28.0 percentage points.

## Why it stopped

Tier 1 direct test produced useful mechanism evidence but not publication-grade support because a stronger transcript-search control saturated the synthetic task.

## Recommended next action

Run one bounded deepen follow-up using human-authored/paraphrased replay traces and equal-token-budget controls against transcript top-1, flat vector retrieval, and scoped-recency flat retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder scoped replay with paraphrased traces and strong flat controls
- Success threshold: Layered memory beats the best non-layered baseline by >= 10 absolute accuracy points, reaches >= 85% overall accuracy, and improves at least 3 of 4 slots without a regression larger than 2 points in any slot.
- Stop condition: Stop as no-paper if transcript or scoped flat retrieval is within 5 accuracy points of layered memory, or if layered gains appear only on generated/template artifacts rather than paraphrased traces.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-agent-replay-for-layered-memory-vs-flat-r-d4ede12428`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
