# Anchor-Aware KV Eviction for CPU Long-Context Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b`
Run ID: `anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b-20260629T032951997781+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

Anchor-window retention achieved 1.0000 query recall and 1.0000 strict span recall in the default proxy, versus 0.0000 for recent-window and sink+recent baselines. A budget sweep showed capacity saturation at 32 cache slots for 48 facts with 0.6646 anchor-window query recall, while center-token recall recovered to 1.0000 at budgets of 48 and above.

## Boundaries and scale limits

No real transformer inference, no natural-language anchor detection, no perplexity or QA accuracy, no CPU serving latency, and no quantized KV implementation were tested. The default confirmation used 64 synthetic trials at sequence length 8192 and cache budget 1024.

## Claim scope

In a deterministic synthetic KV-residency proxy with known distant anchors, anchor-aware retention preserves query-relevant fact tokens under bounded cache budgets where recency and sink+recency policies evict them.

## Why it stopped

Closed as no-paper useful signal because evidence is a synthetic KV-token residency proxy, not full model inference validation.

## Recommended next action

Run a bounded direct integration test in a CPU transformer inference path, using matched KV budgets and long-context QA/retrieval tasks with measured answer accuracy, latency, and memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU inference integration test for anchor-aware KV eviction
- Success threshold: At least a 10 percentage point accuracy improvement over the best matched-budget baseline on a bounded long-context retrieval task, with less than 10 percent decode latency overhead and documented memory parity.
- Stop condition: Stop if integration overhead exceeds 25 percent latency, anchor detection cannot be made deterministic for the test set, or matched-budget accuracy does not beat the best baseline by at least 3 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-aware-kv-eviction-for-cpu-long-context-inference-23c31c04429b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
