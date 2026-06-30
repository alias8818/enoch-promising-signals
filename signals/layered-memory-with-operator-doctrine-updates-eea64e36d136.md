# Layered Memory with Operator-Doctrine Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-with-operator-doctrine-updates-eea64e36d136`
Run ID: `layered-memory-with-operator-doctrine-updates-eea64e36d136-20260620T031303171102+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2b41b650352d

## What looked useful

Across 80 seeds and 1,800 steps per seed, layered_memory reached 0.7825 post-update accuracy versus 0.2312 for flat_episodic and 0.3354 for decayed_flat, while reducing stale-error rate by about 0.39 absolute versus those baselines. Sensitivity runs showed the advantage increased with operator-update coverage.

## Boundaries and scale limits

Evidence is symbolic and synthetic only: no trained language model, natural-language update parser, production retrieval stack, human operator workflow, or long-horizon persistent memory system was tested.

## Claim scope

In a deterministic synthetic doctrine-shift benchmark with partial operator-update visibility, a layered memory policy that separates operator doctrine, versioned episodic examples, and feedback conflict repair improves post-update accuracy and reduces stale-example errors relative to flat and decayed episodic memory baselines.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only in a synthetic proxy, not a direct model or production-agent validation.

## Recommended next action

Run a bounded direct-evidence follow-up using a small RAG or LLM-agent memory stack with natural-language doctrine updates, persistent storage, noisy retrieval, and equal-compute recency/summarization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct RAG-Agent Test of Layered Doctrine Memory Under Natural-Language Updates
- Success threshold: Layered doctrine memory improves post-update accuracy by at least 0.10 absolute over the best non-layered baseline and reduces stale-rule errors by at least 25% relative across at least 5 seeds without increasing overall error.
- Stop condition: Stop if layered memory fails to beat the best baseline on post-update accuracy or stale-rule errors in two independently seeded benchmark configurations, or if update parsing errors dominate the measured effect.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-with-operator-doctrine-updates-eea64e36d136`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
