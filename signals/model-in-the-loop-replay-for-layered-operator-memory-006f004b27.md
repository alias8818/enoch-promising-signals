# Model-in-the-loop replay for layered operator memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `model-in-the-loop-replay-for-layered-operator-memory-006f004b27`
Run ID: `model-in-the-loop-replay-for-layered-operator-memory-006f004b27-20260629T044708537350+0000`

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

- Parent run decision: Layered agent memory with operator-model updates: enoch://control-plane/projects/layered-agent-memory-with-operator-model-updates-b26aa8c35c44/runs/layered-agent-memory-with-operator-model-updates-b26aa8c35c44-20260629T043042072733+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7b7caee9d55

## What looked useful

Layered doctrine/project/decision/artifact memory reached 0.95 mean score and 0.90 exact rate versus flat retrieval at 0.30/0.30; paired bootstrap layered-minus-flat mean score delta was +0.65 with 95% CI [0.45, 0.90].

## Boundaries and scale limits

Small synthetic lexical proxy only; no real operator traces, external LLM answerer, embedding index, long-horizon memory writes, or broad robustness sweep were tested.

## Claim scope

On 8 synthetic operator-memory replay cases with 10 queries, deterministic layer-aware retrieval plus durable-layer answer composition outperformed no-memory, transcript-only, and flat retrieval controls for avoiding stale lower-layer facts.

## Why it stopped

Bounded proxy supports the mechanism but is not direct/full validation of model-in-the-loop operator memory.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with semantic retrieval and a real small/local or API model while preserving the same controls and per-query traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model replay for layered operator memory conflict handling
- Success threshold: Layered memory exact rate at least 0.75 and at least 0.25 absolute exact-rate improvement over flat retrieval, with stale/conflicting forbidden fact leakage below 10%.
- Stop condition: Stop if layered memory fails to beat flat retrieval by at least 0.10 exact rate on the first 30 held-out queries or if model outputs cannot be made reproducible enough for per-query scoring.

## Evidence references

- Artifact root: `<local-path>/projects/model-in-the-loop-replay-for-layered-operator-memory-006f004b27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
