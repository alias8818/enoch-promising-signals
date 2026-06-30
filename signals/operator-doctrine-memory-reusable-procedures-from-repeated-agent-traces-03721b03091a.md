# Operator-Doctrine Memory: Reusable Procedures from Repeated Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-reusable-procedures-from-repeated-agent-traces-03721b03091a`
Run ID: `operator-doctrine-memory-reusable-procedures-from-repeated-agent-traces-03721b03091a-20260621T163202544118+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e9c9627c941

## What looked useful

Cross-domain support plus failure-contrast filtering can recover reusable operator procedures while reducing unsafe or irrelevant carry-over compared with raw transcript search and flat retrieval in this local proxy.

## Boundaries and scale limits

Small hand-authored synthetic corpus; no private operator logs, live agent execution, long-horizon tasks, or robustness tests on noisy natural-language traces.

## Claim scope

On a deterministic synthetic benchmark with 12 repeated agent traces and 6 held-out replay tasks, a layered doctrine memory strategy preserved full procedure recall, avoided forbidden-step false recall, and improved precision by 0.148 over the best full-recall baseline.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism only on a small synthetic replay proxy, not on naturalistic repeated agent traces.

## Recommended next action

Run a bounded deepen test on a larger sanitized real-trace corpus with the same baselines and false-recall scoring; do not write a paper from this synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sanitized Real-Trace Doctrine Memory Replay
- Success threshold: Layered doctrine memory recall >= 0.90, false-recall rate at least 30% lower than transcript_search, and precision at least 0.10 above the best full-recall baseline.
- Stop condition: Stop if layered recall falls below 0.80 or false-recall reduction versus transcript_search is below 10% after the sanitized corpus is labeled.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-reusable-procedures-from-repeated-agent-traces-03721b03091a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
