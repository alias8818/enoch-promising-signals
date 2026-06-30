# Hash-Chained Decision Ledger for Agent Reliability Drift Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea`
Run ID: `hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea-20260529T032721019597+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

Across 300 synthetic drift trials, honest logs detected drift at 94.3% with mean delay 23.4 decisions. Rewriting early post-drift failures delayed the same mutable-log detector to mean delay 117.1 decisions, while anchored ledger verification flagged 100% of rewritten traces. Without anchors, recomputed hash chains passed verification, so anchoring is essential.

## Boundaries and scale limits

Synthetic traces only; no real agent tasks, real evaluator labels, production storage backend, cryptographic signatures, or multi-tenant adversarial environment were tested.

## Claim scope

In a synthetic binary-outcome agent trace benchmark, a hash-chained decision ledger with external anchors detects post-drift log rewrites that otherwise delay reliability drift detection.

## Why it stopped

Synthetic proxy evidence supports the integrity mechanism but is insufficient for a publication-grade reliability drift claim.

## Recommended next action

Run a bounded deepen test on real or recorded agent decision traces with evaluator outcomes and an append-only anchor store; stop this run as synthetic useful-signal evidence, not paper-ready validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored decision ledger replay on real agent incident traces
- Success threshold: Anchored verification flags at least 95% of injected rewrite/omission attacks while preserving drift detection delay within 10% of the honest-log detector on verified traces.
- Stop condition: Stop if anchors cannot detect recomputed-chain mutations, if real traces lack usable outcome labels, or if verified-ledger drift detection is materially worse than the same detector on honest mutable logs.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
