# LLM-in-the-loop exact-anchor memory on realistic multi-session agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199`
Run ID: `llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199-20260613T185004768881+0000`

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

- Parent run decision: Exact-Anchor Compressed Memory for Multi-Session Agent Runs: enoch://control-plane/projects/exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684/runs/exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684-20260613T182327483522+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4d69433c599

## What looked useful

On 3,840 anchored events and 2,585 queries, exact-anchor memory reached 0.9985 accuracy versus 0.1168 for the best baseline, improving by 0.8816 absolute accuracy and clearing the Tier 1 threshold. Top-k ablation stayed above 0.9706 even with k=1.

## Boundaries and scale limits

Generated traces only; deterministic verifier rather than a live LLM; no human-authored production traces, real model hallucination analysis, prompt sensitivity study, or serving cost/latency validation.

## Claim scope

Controlled Tier 1 generated multi-session coding-agent traces show that preserving exact anchor IDs plus local evidence windows and verifier-style constraint matching recovers exact anchors far more reliably than session-chunk lexical retrieval or lossy summary memory.

## Why it stopped

No-paper useful signal: controlled Tier 1 mechanism support is positive, but the verifier and traces are not sufficiently real for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up with a real LLM verifier on archived multi-session agent traces with manually labeled target anchors; stop paper escalation until that direct evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM exact-anchor verification on archived multi-session agent traces
- Success threshold: At least 0.85 exact-anchor accuracy and at least +0.20 absolute accuracy over the best baseline on no fewer than 300 labeled real-trace queries.
- Stop condition: Stop as unsupported if real-LLM exact-anchor memory falls below 0.80 accuracy or fails to beat the best baseline by 0.15 absolute accuracy after prompt calibration on a held-out labeled set.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
