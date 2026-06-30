# Low-Memory Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `low-memory-agent-evidence-ledger-521c7369895f`
Run ID: `low-memory-agent-evidence-ledger-521c7369895f-20260524T205907430216+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/784630b0ac91

## What looked useful

Ledger exact accuracy exceeded sliding-window exact accuracy at every budget: 0.122 vs 0.040 at 1 KB, 0.268 vs 0.077 at 2 KB, 0.738 vs 0.147 at 4 KB, and 1.000 vs 0.277 at 8 KB. Peak Python RSS was 23,276 KB and the bounded CPU run completed locally.

## Boundaries and scale limits

Synthetic only: generated evidence events, simple additive support/refute scoring, no real LLM transcript extraction, no vector-retrieval baseline, no adversarial sources, and no multi-agent concurrency. Main run covered 250 episodes, 240 events per episode, 64 possible claims, and 4,000 scored queries per byte budget.

## Claim scope

In a deterministic synthetic evidence-stream benchmark, a compact claim-indexed evidence ledger preserved final claim status and evidence ids under 1-8 KB serialized state budgets better than a same-byte raw sliding transcript window.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only on synthetic/proxy evidence, not direct real-agent evidence.

## Recommended next action

Run a bounded deepen test on real agent traces with model-based event extraction and compare against vector retrieval plus summary memory before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Trace Benchmark
- Success threshold: At least 20% relative exact-answer improvement over the best baseline at two or more memory budgets, with provenance correctness above 0.80 and extraction failure rate below 0.10.
- Stop condition: Stop if ledger exact accuracy fails to beat the best baseline by at least 5% relative at all tested budgets or if extraction failures exceed 0.25.

## Evidence references

- Artifact root: `<local-path>/projects/low-memory-agent-evidence-ledger-521c7369895f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
