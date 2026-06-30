# LLM-in-the-loop hash-pinned quote memory under noisy repeated sessions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1`
Run ID: `llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1-20260621T120752308955+0000`

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

- Parent run decision: Anchored Long-Context: Hash-Pinned Quote Memory: enoch://control-plane/projects/anchored-long-context-hash-pinned-quote-memory-c2e888158f43/runs/anchored-long-context-hash-pinned-quote-memory-c2e888158f43-20260621T114604638743+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Hash-pinning exact quote spans is a promising mechanism for quote-memory integrity under repeated noisy sessions, but this run is not paper-ready because the noisy LLM behavior and conversations were simulated.

## Boundaries and scale limits

Small CPU-only synthetic run: 120 primary tasks, 480 recall decisions, no live LLM calls, no production traces, no human adjudication, and simple deterministic retrieval/summary baselines.

## Claim scope

In a deterministic synthetic repeated-session benchmark with exact quoted facts, noisy repeats, distractor quotes, and simple matched baselines, hash-pinned quote memory achieved perfect exact recall and zero wrong hash-verified answers; intentional stored-quote tampering produced abstentions rather than wrong verified recalls.

## Why it stopped

Mechanism-supporting useful signal only; synthetic Tier-1 evidence is not publication-grade validation.

## Recommended next action

Run a bounded live-LLM deepen follow-up using the same hash-pinned quote policy, exact-recall metric, contamination baselines, and tamper-abstention audit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-LLM hash-pinned quote memory under noisy repeated sessions
- Success threshold: Hash-pinned quote memory exact_rate >= 0.95, wrong_hash_verified_answers = 0, and exact-rate lift >= 0.20 over both baselines on at least 300 live-LLM recall decisions.
- Stop condition: Stop if live-LLM exact recall falls below 0.90, any wrong hash-verified answer appears, or the lift over either baseline is below 0.10 after the planned recall decisions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-hash-pinned-quote-memory-under-noisy-repea-e31d208eb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
