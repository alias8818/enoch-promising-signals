# Predictive Operator-Model Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `predictive-operator-model-agent-memory-2e47fe3f6f8c`
Run ID: `predictive-operator-model-agent-memory-2e47fe3f6f8c-20260628T103524197657+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9dde20d17e26

## What looked useful

Layered doctrine memory reached 0.8536 mean accuracy over 7,680 held-out cases, beating the best baseline by 0.1966 and beating its shuffled-history control by 0.3786.

## Boundaries and scale limits

Synthetic data only; rule-based memory strategies only; no real operator logs, LLM agent loop, production privacy constraints, long-horizon memory decay, or full-scale deployment workload.

## Claim scope

In a deterministic synthetic repeated-session replay with stable latent operator preferences, noisy prior episodes, and held-out next-action labels, a layered operator-doctrine memory strategy improved preference prediction over no-memory, transcript-search, and flat-retrieval baselines and degraded under shuffled-history control.

## Why it stopped

Useful synthetic mechanism evidence was produced, but the result is not paper-ready because it is proxy-only and lacks real operator/session validation.

## Recommended next action

Run a bounded deepen follow-up on a small human-labeled or realistic repeated-session replay corpus with the same baselines and shuffled-history control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-labeled repeated-session operator preference replay
- Success threshold: Layered memory beats the best baseline by at least 0.05 absolute accuracy and beats shuffled-history control by at least 0.10 on held-out future actions.
- Stop condition: Stop as negative if layered memory fails either threshold or if labels cannot distinguish stable operator preference from scenario priors.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-agent-memory-2e47fe3f6f8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
