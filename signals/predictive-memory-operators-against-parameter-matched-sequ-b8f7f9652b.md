# Predictive memory operators against parameter-matched sequence-model controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `predictive-memory-operators-against-parameter-matched-sequ-b8f7f9652b`
Run ID: `predictive-memory-operators-against-parameter-matched-sequ-b8f7f9652b-20260620T071726119966+0000`

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

- Parent run decision: Predictive Operator-Model Memory Updates: enoch://control-plane/projects/predictive-operator-model-memory-updates-512071ff306f/runs/predictive-operator-model-memory-updates-512071ff306f-20260620T065702032104+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/86bb76839617

## What looked useful

Across 3 seeds, PMO achieved 100.0% accuracy at train delay 24 and extrapolated delay 96, while the 45.4k-parameter GRU control achieved 3.38% and 3.35% respectively; the 50.3k-parameter mean-pool sanity control reached 15.47% and 7.71%.

## Boundaries and scale limits

Synthetic grammar-aligned task only; exact key slots are provided to the PMO; no natural language modeling, GPT-2-small-class transformer baseline, learned parsing stress test, or large-scale training was performed.

## Claim scope

On a small synthetic key/value associative recall benchmark with 12 distractor pairs and delayed query, an explicit key-indexed predictive memory operator substantially outperformed a near parameter-matched GRU control under the same training budget.

## Why it stopped

Tier 1 direct test met the bounded mechanism threshold, but evidence remains synthetic and architecture-prior-heavy, so this is a no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a fairer bounded follow-up that gives controls equivalent grammar hints or attention/retrieval capacity and tests randomized query positions before considering any paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grammar-matched controls for predictive memory associative recall
- Success threshold: PMO keeps at least a 10 absolute accuracy point advantage over the strongest grammar-matched control on the long-delay split without losing in-distribution accuracy.
- Stop condition: Stop if grammar-matched controls close the long-delay gap below 10 absolute accuracy points or if PMO fails randomized-query evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-memory-operators-against-parameter-matched-sequ-b8f7f9652b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
