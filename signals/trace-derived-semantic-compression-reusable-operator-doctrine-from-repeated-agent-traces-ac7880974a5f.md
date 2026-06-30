# Trace-Derived Semantic Compression: Reusable Operator Doctrine From Repeated Agent Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-semantic-compression-reusable-operator-doctrine-from-repeated-agent-traces-ac7880974a5f`
Run ID: `trace-derived-semantic-compression-reusable-operator-doctrine-from-repeated-agent-traces-ac7880974a5f-20260621T112722206316+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8350c477ab3d

## What looked useful

Reusable operator coding can outperform exact step memorization on synthetic repeated traces, especially for compression, but evidence is proxy-only and one robustness seed underperformed memorization on F1.

## Boundaries and scale limits

No real repeated agent trace corpus with independent semantic labels was available. The experiment used synthetic traces, a small local Codex JSONL event probe, CPU-only standard-library scripts, and no downstream agent task replay.

## Claim scope

On a deterministic synthetic benchmark of repeated agent workflows, a mined operator doctrine compressed held-out unseen-domain traces to a mean 0.121 token ratio over 20 seeds while preserving hidden operator labels with mean 0.957 macro-F1.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy evidence, not direct validation on real repeated agent traces.

## Recommended next action

Run a bounded deepen follow-up on 50-100 real agent traces with independent semantic step labels and compare doctrine compression against exact memorization, LLM summaries, and raw traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Operator Doctrine Validation
- Success threshold: Operator doctrine achieves >=0.85 macro-F1 on held-out real traces, >=50% token reduction versus raw traces, and non-inferior downstream replay quality versus raw trace context.
- Stop condition: Stop if held-out real-trace macro-F1 is <0.70 or token reduction is <30% after a fixed preprocessing and threshold sweep.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-reusable-operator-doctrine-from-repeated-agent-traces-ac78809`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
